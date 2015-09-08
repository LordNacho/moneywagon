# -*- coding: utf-8 -*-
from __future__ import print_function

from binascii import unhexlify, hexlify
from hashlib import sha256
from unicodedata import normalize
import sys

from moneywagon.core import get_magic_bytes
from bitcoin import (
    privtopub, pubtoaddr, encode_privkey, get_privkey_format,
    encode_pubkey, changebase, fast_multiply, G
)

try:
    import scrypt
except ImportError:
    raise ImportError("Scrypt is required for BIP38 support: pip install scrypt")

try:
    from Crypto.Cipher import AES
except ImportError:
    raise ImportError("Pycrypto is required for bip38 support: pip install pycrypto")

is_py2 = False
if sys.version_info <= (3,0):
    # py2
    is_py2 = True
else:
    # py3
    long = int
    unicode = str

def base58check(payload):
    checksum = sha256(sha256(payload).digest()).digest()[:4] # b58check for encrypted privkey
    return changebase(hexlify(payload + checksum).decode('ascii'), 16, 58)


def bip38_encrypt(crypto, privkey, passphrase):
    """
    BIP0038 non-ec-multiply encryption. Returns BIP0038 encrypted privkey.
    """
    pub_byte, priv_byte = get_magic_bytes(crypto)
    privformat = get_privkey_format(privkey)
    if privformat in ['wif_compressed','hex_compressed']:
        compressed = True
        flagbyte = b'\xe0'
        if privformat == 'wif_compressed':
            privkey = encode_privkey(privkey,'hex_compressed')
            privformat = get_privkey_format(privkey)
    if privformat in ['wif', 'hex']:
        compressed = False
        flagbyte = b'\xc0'
    if privformat == 'wif':
        privkey = encode_privkey(privkey,'hex')
        privformat = get_privkey_format(privkey)

    pubkey = privtopub(privkey)
    addr = pubtoaddr(pubkey, pub_byte)

    passphrase = normalize('NFC', unicode(passphrase))
    if is_py2:
        ascii_key = addr
        passphrase = passphrase.encode('utf8')
    else:
        ascii_key = bytes(addr,'ascii')

    salt = sha256(sha256(ascii_key).digest()).digest()[0:4]
    key = scrypt.hash(passphrase, salt, 16384, 8, 8)
    derivedhalf1, derivedhalf2 = key[:32], key[32:]

    aes = AES.new(derivedhalf2)
    encryptedhalf1 = aes.encrypt(unhexlify('%0.32x' % (long(privkey[0:32], 16) ^ long(hexlify(derivedhalf1[0:16]), 16))))
    encryptedhalf2 = aes.encrypt(unhexlify('%0.32x' % (long(privkey[32:64], 16) ^ long(hexlify(derivedhalf1[16:32]), 16))))

    payload = b'\x01\x42' + flagbyte + salt + encryptedhalf1 + encryptedhalf2
    return base58check(payload)


def bip38_decrypt(crypto, encrypted_privkey, passphrase, wif=False):
    """
    BIP0038 non-ec-multiply decryption. Returns hex privkey.
    """
    pub_byte, priv_byte = get_magic_bytes(crypto)
    passphrase = normalize('NFC', unicode(passphrase))
    if is_py2:
        passphrase = passphrase.encode('utf8')

    d = unhexlify(changebase(encrypted_privkey, 58, 16, 86))

    # trim off first 2 bytes (0x01c) (\x01\x42)
    d = d[2:]
    flagbyte = d[0:1]
    d = d[1:]
    # respect flagbyte, return correct pair

    if flagbyte == b'\xc0':
        compressed = False
    elif flagbyte == b'\xe0':
        compressed = True
    else:
        raise Exception("Only non-ec mode at this time.")

    addresshash = d[0:4]
    d = d[4:-4]
    key = scrypt.hash(passphrase,addresshash, 16384, 8, 8)
    derivedhalf1 = key[0:32]
    derivedhalf2 = key[32:64]
    encryptedhalf1 = d[0:16]
    encryptedhalf2 = d[16:32]
    aes = AES.new(derivedhalf2)
    decryptedhalf2 = aes.decrypt(encryptedhalf2)
    decryptedhalf1 = aes.decrypt(encryptedhalf1)
    priv = decryptedhalf1 + decryptedhalf2
    priv = unhexlify('%064x' % (long(hexlify(priv), 16) ^ long(hexlify(derivedhalf1), 16)))
    pub = privtopub(priv)
    if compressed:
        pub = encode_pubkey(pub,'hex_compressed')
    addr = pubtoaddr(pub, pub_byte)

    if is_py2:
        ascii_key = addr
    else:
        ascii_key = bytes(addr,'ascii')

    if sha256(sha256(ascii_key).digest()).digest()[0:4] != addresshash:
        raise Exception('Bip38 password decrypt failed: Wrong password?')
    else:
        formatt = 'wif' if wif else 'hex'
        if compressed:
            return encode_privkey(priv, formatt + '_compressed')
        else:
            return encode_privkey(priv, formatt)

def compress(x, y):
    """
    Given a x,y coordinate, encode in "compressed format"
    """
    polarity = "02" if y % 2 == 0 else "03"
    return "%s%x" % (polarity, x)

def bip38_generate_intermediate_point(passphrase, seed, lot=None, sequence=None):
    passphrase = normalize('NFC', unicode(passphrase))
    if is_py2:
        passphrase = passphrase.encode('utf8')

    if not is_py2:
        seed = bytes(seed, 'ascii')

    if lot and sequence:
        ownersalt = sha256(seed).digest()[:4]
        lotseq = unhexlify("%0.8x" % (4096 * lot + sequence))
        ownerentropy = ownersalt + lotseq
    else:
        ownersalt = ownerentropy = sha256(seed).digest()[:8]

    prefactor = scrypt.hash(passphrase, ownersalt, 16384, 8, 8, 32)

    if lot and sequence:
        passfactor = sha256(sha256(prefactor + ownerentropy).digest()).digest()
    else:
        passfactor = prefactor

    if is_py2:
        as_int = int(prefactor.encode('hex'), 16)
    else:
        as_int = int.from_bytes(prefactor, byteorder='big')

    ppx, ppy = fast_multiply(G, as_int)
    passpoint = compress(ppx, ppy) # 33 byte compressed format starting with 02 or 03

    if not is_py2:
        passpoint = bytes(passpoint, 'ascii')

    last_byte = b'\x53' if not lot and not sequence else b'\x51'
    magic_bytes = b'\x2C\xE9\xB3\xE1\xFF\x39\xE2' + last_byte # 'passphrase' prefix
    payload = magic_bytes + ownerentropy + unhexlify(passpoint)
    return base58check(payload)

def ec_test():
    """
    Tests the ec-multiply sections. Cases taken from the bip38 document.
    """
    cases = [[
        'btc',
        'TestingOneTwoThree',
        'passphrasepxFy57B9v8HtUsszJYKReoNDV6VHjUSGt8EVJmux9n1J3Ltf1gRxyDGXqnf9qm',
        '6PfQu77ygVyJLZjfvMLyhLMQbYnu5uguoJJ4kMCLqWwPEdfpwANVS76gTX',
        '1PE6TQi6HTVNz5DLwB1LcpMBALubfuN2z2',
        '5K4caxezwjGCGfnoPTZ8tMcJBLB7Jvyjv4xxeacadhq8nLisLR2',
        ],[
        'btc',
        'Satoshi',
        'passphraseoRDGAXTWzbp72eVbtUDdn1rwpgPUGjNZEc6CGBo8i5EC1FPW8wcnLdq4ThKzAS',
        '6PfLGnQs6VZnrNpmVKfjotbnQuaJK4KZoPFrAjx1JMJUa1Ft8gnf5WxfKd',
        '1CqzrtZC6mXSAhoxtFwVjz8LtwLJjDYU3V',
        '5KJ51SgxWaAYR13zd9ReMhJpwrcX47xTJh2D3fGPG9CM8vkv5sH',
    ]]

    cases = [[
        'btc',
        'MOLON LABE',
        'passphraseaB8feaLQDENqCgr4gKZpmf4VoaT6qdjJNJiv7fsKvjqavcJxvuR1hy25aTu5sX',
        '6PgNBNNzDkKdhkT6uJntUXwwzQV8Rr2tZcbkDcuC9DZRsS6AtHts4Ypo1j',
        '1Jscj8ALrYu2y9TD8NrpvDBugPedmbj4Yh',
        '5JLdxTtcTHcfYcmJsNVy1v2PMDx432JPoYcBTVVRHpPaxUrdtf8',
        'cfrm38V8aXBn7JWA1ESmFMUn6erxeBGZGAxJPY4e36S9QWkzZKtaVqLNMgnifETYw7BPwWC9aPD',
        263183,
        1
        ],[
        'btc',
        'ΜΟΛΩΝ ΛΑΒΕ',
        'passphrased3z9rQJHSyBkNBwTRPkUGNVEVrUAcfAXDyRU1V28ie6hNFbqDwbFBvsTK7yWVK',
        '6PgGWtx25kUg8QWvwuJAgorN6k9FbE25rv5dMRwu5SKMnfpfVe5mar2ngH',
        '1Lurmih3KruL4xDB5FmHof38yawNtP9oGf'
        '5KMKKuUmAkiNbA3DazMQiLfDq47qs8MAEThm4yL8R2PhV1ov33D',
        'cfrm38V8G4qq2ywYEFfWLD5Cc6msj9UwsG2Mj4Z6QdGJAFQpdatZLavkgRd1i4iBMdRngDqDs51',
        806938,
        1
    ]]


def non_ec_test():
    # taken directly from the BIP38 whitepaper
    cases = [[
        'btc',
        '6PRVWUbkzzsbcVac2qwfssoUJAN1Xhrg6bNk8J7Nzm5H7kxEbn2Nh2ZoGg',
        'cbf4b9f70470856bb4f40f80b87edb90865997ffee6df315ab166d713af433a5',
        u'TestingOneTwoThree',
        False
        ], [
        'btc',
        '6PRNFFkZc2NZ6dJqFfhRoFNMR9Lnyj7dYGrzdgXXVMXcxoKTePPX1dWByq',
        '09c2686880095b1a4c249ee3ac4eea8a014f11e6f986d0b5025ac1f39afbd9ae',
        u'Satoshi',
        False
        ],[
        'btc',
        '6PRW5o9FLp4gJDDVqJQKJFTpMvdsSGJxMYHtHaQBF3ooa8mwD69bapcDQn',
        '5Jajm8eQ22H3pGWLEVCXyvND8dQZhiQhoLJNKjYXk9roUFTMSZ4',
        u'\u03D2\u0301\u0000\U00010400\U0001F4A9',
        True,
        ],[
        'btc',
        '6PYNKZ1EAgYgmQfmNVamxyXVWHzK5s6DGhwP4J5o44cvXdoY7sRzhtpUeo',
        'L44B5gGEpqEDRS9vVPz7QT35jcBG2r3CZwSwQ4fCewXAhAhqGVpP',
        u'TestingOneTwoThree',
        True
        ],[
        'btc',
        '6PYLtMnXvfG3oJde97zRyLYFZCYizPU5T3LwgdYJz1fRhh16bU7u6PPmY7',
        'KwYgW8gcxj1JWJXhPSu4Fqwzfhp5Yfi42mdYmMa4XqK7NJxXUSK7',
        u'Satoshi',
        True
    ]]

    index = 1
    for crypto, encrypted_key, unencrypted_key, password, use_wif in cases:
        test_encrypted = bip38_encrypt(crypto, unencrypted_key, password)
        test_decrypted = bip38_decrypt(crypto, encrypted_key, password, wif=use_wif)
        assert encrypted_key == test_encrypted, "encrypt failed"
        assert unencrypted_key == test_decrypted, 'decrypt failed'
        print("Test #%s passed" % index)
        index += 1

def test():
    #ec_test()
    non_ec_test()