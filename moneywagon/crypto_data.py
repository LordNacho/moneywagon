from datetime import datetime
from .services import *
from moneywagon.core import make_standard_halfing_eras

# instructions for getting version byte:
# https:/github.com/MichaelMure/WalletGenerator.net/wiki/How-to-add-a-new-currency#step-two-find-the-prefixes-for-the-address-format-of-your-currency

# also here: https://github.com/MichaelMure/WalletGenerator.net/blob/master/src/janin.currency.js#L78

crypto_data = {
    'btc': {
        'name': 'Bitcoin',
        'address_version_byte': 0, # base58Prefixes[PUBKEY_ADDRESS] in chainparams.cpp
        'message_magic': b"\xf9\xbe\xb4\xd9", # pchMessageStart in chainparams.cpp
        'bip44_coin_type': 0x80000000,
        'private_key_prefix': 128,  # base58Prefixes[SECRET_KEY] in chainparams.cpp
        'genesis_date': datetime(2009, 1, 3, 18, 15, 5),
        'supply_data': {
            'method': 'standard',
            'start_coins_per_block': 50,
            'minutes_per_block': 10,
            'full_cap': 21000000,
            'blocks_per_era': 210000,
            'reward_ends_at_block': 6930000
        },
        'services': {
            'current_price': {
                'usd': [
                    Bitstamp, GDAX, BTCE, Gemini, Huobi, Bittrex, CexIO, YoBit,
                    Poloniex, Winkdex, ChainSo, Kraken, xBTCe, Vircurex
                ],
                'cny': [BTER, BTCChina, Huobi, xBTCe, BTC38, ChainSo],
                'rur': [BTCE], 'jpy': [Kraken, xBTCe], 'gbp': [Kraken, xBTCe],
                'eur': [Bitstamp, xBTCe, UseCryptos, Kraken, ChainSo], 'cad': [Kraken],
                'idr': [BitcoinIndonesia], 'mxn': [Bitso], 'bgn': [CryptoBG],
                'krw': [CoinOne], '*': [Cryptonator, Yunbi]
            },
            'address_balance': [
                BlockCypher, Blockr, ChainSo,
                BitEasy, SmartBitAU, BlockExplorerCom, BlockChainInfo, Blockonomics,
                BitpayInsight, CoinPrism, BitGo, LocalBitcoinsChain, Bchain
            ],
            'historical_transactions': [
                Blockr, BlockExplorerCom, BitGo, SmartBitAU, ChainSo, CoinPrism, BlockSeer,
                BitpayInsight, Blockonomics, LocalBitcoinsChain
            ],
            'single_transaction': [
                BitpayInsight, Blockr, BlockCypher, BlockExplorerCom,
                ChainSo, CoinPrism, SmartBitAU, LocalBitcoinsChain
            ],
            'push_tx': [
                BlockChainInfo, BlockExplorerCom, Blockr, ChainSo, CoinPrism,
                BitpayInsight, LocalBitcoinsChain
            ],
            'unspent_outputs': [
                Blockr, BitpayInsight, BlockExplorerCom, SmartBitAU, BlockChainInfo, CoinPrism, ChainSo,
                BitGo, LocalBitcoinsChain
            ],
            'get_block': [
                BitpayInsight, ChainRadar, Blockr, OKcoin, BlockExplorerCom, ChainSo,
                BitGo, LocalBitcoinsChain
            ],
            "get_optimal_fee": [
                BitGo, BlockCypher, CoinTape, BitcoinFees21
            ]
        },
    },
    'ltc': {
        'name': 'Litecoin',
        'address_version_byte': 48,
        'message_magic': b"\xfb\xc0\xb6\xdb",
        'bip44_coin_type': 0x80000002,
        'private_key_prefix': 176,
        'genesis_date': datetime(2011, 10, 7),
        'supply_data': {
            'method': 'standard',
            'start_coins_per_block': 50,
            'minutes_per_block': 2.5,
            'full_cap': 84000000,
            'blocks_per_era': 840000
        },
        'services': {
            'current_price': {
                'usd': [
                    BTCE, GDAX, Poloniex, Kraken, Cryptopia, CexIO, ChainSo,
                    xBTCe, YoBit, UseCryptos
                ],
                'cny': [BTCE, Huobi, BTER, xBTCe, ChainSo, OKcoin, BTC38, BTCChina],
                'rur': [YoBit, xBTCe], 'eur': [Kraken, BTCE, GDAX, UseCryptos, xBTCe],
                'btc': [
                    GDAX, BTCE, CexIO, BTER, BleuTrade, Bittrex, Poloniex,
                    ChainSo, xBTCe, YoBit, Cryptopia, Kraken, NovaExchange,
                    BitcoinIndonesia, BTCChina, Liqui
                ],
                'doge': [CexIO], 'xmr': [Poloniex], 'jpy': [xBTCe], 'nzd': [Cryptopia],
                '*': [Cryptonator, Vircurex, YoBit],
            },
            'address_balance': [
                BlockCypher, Blockr, ChainSo, ProHashing, HolyTransaction, Bchain
            ],
            'historical_transactions': [
                ProHashing, Blockr, ChainSo
            ],
            'single_transaction': [
                Blockr, BlockCypher
            ],
            'push_tx': [
                Blockr, ChainSo
            ],
            'unspent_outputs': [
                ChainSo, Blockr
            ],
            'get_block': [
                ChainSo, Blockr, OKcoin, ProHashing, HolyTransaction
            ],
            "get_optimal_fee": [
                BlockCypher
            ]
        },
    },
    'ppc': {
        'name': 'Peercoin',
        'address_version_byte': 55,
        'message_magic': b"\xe6\xe8\xe9\xe5",
        'bip44_coin_type': 0x80000006,
        'private_key_prefix': 183,
        'proof_of_stake': True,
        'genesis_date': datetime(2012, 8, 19, 18, 12, 4),
        'supply_data': {},
        'services': {
            'current_price': {
                'usd': [BTCE, xBTCe, ChainSo], 'eur': [UseCryptos],
                'btc': [
                    BTCE, xBTCe, BleuTrade, ChainSo, Bittrex, BTER, Poloniex, Vircurex,
                    YoBit, UseCryptos
                ], 'doge': [BleuTrade], 'cny': [BTC38],
                '*': [Cryptonator]
            },
            'address_balance': [Blockr, Mintr, HolyTransaction],
            'historical_transactions': [Blockr],
            'single_transaction': [Mintr, Blockr],
            'push_tx': [MultiCoins],
            'unspent_outputs': [Blockr],
            'get_block': [Mintr, HolyTransaction]
        },
    },
    'doge': {
        'name': 'Dogecoin',
        'message_magic': b"\xc0\xc0\xc0\xc0",
        'address_version_byte': 30,
        'bip44_coin_type': 0x80000003,
        'private_key_prefix': 158,
        'genesis_date': datetime(2013, 12, 6, 10, 25, 40),
        'supply_data': {
            'method': 'per_era',
            'eras': [
                {'start': 1,      'end': 100000, 'reward': 500000}, # reward was random, average used
                {'start': 100001, 'end': 144999, 'reward': 250011}, # reward was random, average used
                {'start': 145000, 'end': 200000, 'reward': 250000},
                ] + make_standard_halfing_eras(
                    start=200000, interval=100000,
                    start_reward=125000, total_eras=4
                ) + [
                {'start': 600001, 'end': None,   'reward': 10000}
            ],
            'minutes_per_block': 1.0,
            'full_cap': None,
        },
        'services': {
            'current_price': {
                'usd': [CexIO], 'cny': [BTC38],
                'rur': [YoBit], 'ltc': [NovaExchange],
                'btc': [
                    Bittrex, Poloniex, BleuTrade, ChainSo, BTER, YoBit,
                    NovaExchange, Vircurex, BitcoinIndonesia, UseCryptos
                ],
                '*': [Cryptonator],
            },
            'address_balance': [
                BlockCypher, ChainSo, DogeChainInfo, ProHashing, HolyTransaction,
                Bchain
            ],
            'historical_transactions': [
                BlockCypher, ChainSo, ProHashing
            ],
            'single_transaction': [
                BlockCypher, ChainSo
            ],
            'push_tx': [
                ChainSo
            ],
            'unspent_outputs': [
                DogeChainInfo, ChainSo
            ],
            'get_block': [
                ChainSo, ProHashing, HolyTransaction
            ]
        },
    },
    'nxt': {
        'name': 'Nxt',
        'address_version_byte': None,
        'bip44_coin_type': 0x8000001d,
        'private_key_prefix': None,
        'genesis_date': datetime(2013, 10, 29),
        'services': {
            'current_price': {
                'btc': [Bittrex, BitcoinIndonesia, ChainSo, Poloniex],
                '*': [Cryptonator], 'cny': [BTC38],
            },
            'address_balance': [MyNXT, NXTPortal],
            'historical_transactions': [NXTPortal],
            'single_transaction': [],
            'push_tx': [],
            'unspent_outputs': [],
            'get_block': []
        },
    },
    'xmy': {
        'name': 'MyriadCoin',
        'address_version_byte': 50,
        'message_magic': b"\xaf\x45\x76\xee",
        'bip44_coin_type': 0x8000005a,
        'private_key_prefix': 178,
        'genesis_date': datetime(2014, 2, 23),
        'supply_data': {
            'method': 'standard',
            'start_coins_per_block': 1000,
            'minutes_per_block': 0.5,
            'full_cap': 2000000000,
            'blocks_per_era': 967680
        },
        'services': {
            'current_price': {
                'btc': [Bittrex, Cryptopia], 'ltc': [Cryptopia],
                'doge': [Cryptopia], 'uno': [Cryptopia],
                '*': [Cryptonator]
            },
            'address_balance': [
                MYRCryptap, CryptapUS, BirdOnWheels, ProHashing
            ],
            'historical_transactions': [
                MYRCryptap, BirdOnWheels, ProHashing
            ],
            'single_transaction': [
                MYRCryptap, BirdOnWheels
            ],
            'push_tx': [
                MYRCryptap, BirdOnWheels
            ],
            'unspent_outputs': [
                MYRCryptap, BirdOnWheels
            ],
            'get_block': [
                MYRCryptap, BirdOnWheels, ProHashing
            ]
        },
    },
    'vtc': {
        'name': 'Vertcoin',
        'address_version_byte': 71,
        'message_magic': b"\xfa\xbf\xb5\xda",
        'bip44_coin_type': 0x8000001c,
        'private_key_prefix': 199,
        'genesis_date': datetime(2014, 1, 8),
        'supply_data': {
            'method': 'standard',
            'start_coins_per_block': 50,
            'minutes_per_block': 2.5,
            'full_cap': 84000000,
            'blocks_per_era': 840000
        },
        'services': {
            'current_price': {
                'btc': [Poloniex, Bittrex, ChainSo, BleuTrade, YoBit],
                'doge': [BleuTrade],
                '*': [Cryptonator],
            },
            'address_balance': [Bchain, VTConline],
            'historical_transactions': [VTConline],
            'single_transaction': [VTConline],
            'push_tx': [],
            'unspent_outputs': [],
            'get_block': [VTConline]
        },
    },
    'ftc': {
        'name': 'Feathercoin',
        'address_version_byte': 14,
        'message_magic': b"\xfb\xc0\xb6\xdb",
        'bip44_coin_type': 0x80000008,
        'private_key_prefix': 0x8e,
        'genesis_date': datetime(2013, 4, 16),
        'supply_data': {
            'method': 'per_era',
            'minutes_per_block': 2.5,
            'eras': [
                {'start': 0,      'end': 204638, 'reward': 200},
                {'start': 204639, 'end': 2100000, 'reward': 80}
            ] + make_standard_halfing_eras(
                start=2100000, interval=2100000,
                start_reward=40
            ),
            'blocktime_adjustments': [
                [0, 2.632061418725984],
                [204639, 1]
            ],
            'full_cap': 336000000,
            'blocks_per_era': 2100000,
        },
        'services': {
            'current_price': {
                'btc': [Bittrex, ChainSo, Cryptonator, Vircurex],
                'ltc': [Cryptopia], 'doge': [Cryptopia], 'uno': [Cryptopia],
                '*': [Cryptonator]
            },
            'address_balance': [
                ChainTips, FeathercoinCom2, Bchain
            ],
            'historical_transactions': [
                ChainTips, ProHashing
            ],
            'single_transaction': [
                ChainTips
            ],
            'push_tx': [
                ChainTips
            ],
            'unspent_outputs': [
                ChainTips
            ],
            'get_block': [
                ChainTips, ProHashing
            ]
        },
    },
    'dash': {
        'name': 'Dash',
        'address_version_byte': 76,
        "message_magic": b"\xbf\x0c\x6b\xbd",
        'bip44_coin_type': 0x80000005,
        'private_key_prefix': 204,
        'genesis_date': datetime(2014, 1, 19, 1, 40, 18),
        'supply_data': {
            'method': 'per_era',
            'eras': [
                {'start': 1,   'end': 5000,  'reward': 500}, # "instamine"
                {'start': 5001, 'end': 20000,  'reward': 144},
                {'start': 20001, 'end': 60000, 'reward': 14}
            ] + make_standard_halfing_eras(
                start=60000, interval=210240,
                start_reward=5, halfing_func=lambda era, reward: reward - ((reward/14) * era)
            ),
            'additional_block_interval_adjustment_points': [
                 100, 500, 1000, 3000, 5000
            ],
            'minutes_per_block': 2.5,
            'full_cap': 18900000,
        },
        'services': {
            'current_price': {
                'usd': [CexIO, Cryptopia, Kraken, xBTCe, Liqui],
                'doge': [NovaExchange, Cryptopia, BleuTrade], 'eth': [Liqui],
                'rur': [YoBit], 'ltc': [NovaExchange, Cryptopia, CexIO],
                'btc': [
                    Bittrex, Poloniex, Cryptopia, ChainSo, YoBit, CexIO, BleuTrade,
                    NovaExchange, Kraken, UseCryptos, Liqui
                ], 'cny': [xBTCe, BTC38], 'eur': [UseCryptos, Kraken],
                '*': [Cryptonator], 'uno': [Cryptopia], 'moon': [NovaExchange]
            },
            'address_balance': [
                CryptoID, ProHashing, MasterNodeIO, SiampmDashInsight, HolyTransaction,
                DashOrgInsight
            ],
            'historical_transactions': [
                ProHashing, DashOrgInsight, SiampmDashInsight, MasterNodeIO
            ],
            'single_transaction': [
                DashOrgInsight, SiampmDashInsight, MasterNodeIO, CryptoID
            ],
            'push_tx': [
                MasterNodeIO, DashOrgInsight, SiampmDashInsight
            ],
            'unspent_outputs': [
                MasterNodeIO, SiampmDashInsight, DashOrgInsight, CryptoID
            ],
            'get_block': [
                ProHashing, SiampmDashInsight, HolyTransaction, MasterNodeIO,
                DashOrgInsight
            ]
        },
    },
    'rdd': {
        'name': 'Reddcoin',
        'address_version_byte': 61,
        'bip44_coin_type': 0x80000004,
        'private_key_prefix': 0xbd,
        'genesis_date': datetime(2014, 1, 20),
        'proof_of_stake': True,
        'services': {
            'current_price': {
                'btc': [Bittrex, YoBit, BleuTrade, Cryptopia, NovaExchange],
                'ltc': [Cryptopia, NovaExchange], 'esp2': [NovaExchange],
                'doge': [Cryptopia, BleuTrade], 'uno': [Cryptopia], '*': [Cryptonator]
            },
            'address_balance': [ReddcoinCom, ProHashing],
            'historical_transactions': [ReddcoinCom, ProHashing],
            'single_transaction': [ReddcoinCom],
            'push_tx': [ReddcoinCom],
            'unspent_outputs': [ReddcoinCom],
            'get_block': [ReddcoinCom, ProHashing]
        },
    },

    'nmc': {
        'name': 'Namecoin',
        'address_version_byte': 52,
        'bip44_coin_type': 0x80000007,
        'private_key_prefix': 0x80,
        'genesis_date': datetime(2011, 4, 18),
        'services': {
            'current_price': {
                'btc': [Poloniex, BleuTrade, YoBit, xBTCe, Cryptopia, Vircurex],
                'ltc': [Cryptopia], 'usd': [xBTCe],
                'doge': [Cryptopia, BleuTrade], 'uno': [Cryptopia], '*': [Cryptonator]
            },
            'address_balance': [WebBTC, Bchain]
        }
    },
    'aur': {
        'name': 'Auroracoin',
        'address_version_byte': 23,
        'bip44_coin_type': 0x80000055,
        'private_key_prefix': 0x97,
        'genesis_date': datetime(2014, 2, 2),
        'services': {
            'current_price': {
                'btc': [Bittrex, YoBit, Cryptopia], 'ltc': [Cryptopia],
                'doge': [Cryptopia], 'uno': [Cryptopia], '*': [Cryptonator]
            },
            'address_balance': [CryptoID, ProHashing],
            'historical_transactions': [ProHashing],
            'single_transaction': [CryptoID],
            'push_tx': [],
            'unspent_outputs': [CryptoID],
            'get_block': []
        },
    },

    'emc': {
        'name': 'Emercoin',
        'address_version_byte': 33,
        'bip44_coin_type': None,
        'private_key_prefix': 128,
        'message_magic': b"\xe6\xe8\xe9\xe5",
        'genesis_date': datetime(2011, 11, 5),
        'github_link': "https://github.com/emercoin/emercoin",
        'services': {
            'current_price': {
                'btc': [YoBit, Bittrex, xBTCe, Cryptopia], 'ltc': [Cryptopia],
                'usd': [xBTCe], 'cny': [BTC38],
                'doge': [Cryptopia], 'uno': [Cryptopia], '*': [Cryptonator]
            },
            'address_balance': [Mintr],
            'historical_transactions': [],
            'single_transaction': [Mintr],
            'push_tx': [],
            'unspent_outputs': [],
            'get_block': [Mintr]
        },
    },

    'gsm': {
        'name': 'GSMcoin',
        'address_version_byte': 38,
        'bip44_coin_type': None,
        'private_key_prefix': 166,
        'genesis_date': datetime(1, 1, 1),
        'github_link': "https://github.com/gsmcoin/GSMcoin",
        'services': {
            'current_price': {'btc': [YoBit]},
            'address_balance': [],
            'historical_transactions': [],
            'single_transaction': [],
            'push_tx': [],
            'unspent_outputs': [],
            'get_block': []
        },
    },

    'erc': {
        'name': 'Europecoin',
        'address_version_byte': 33,
        'bip44_coin_type': None,
        'private_key_prefix': 161,
        'genesis_date': datetime(1, 1, 1),
        'github_link': "https://github.com/EuropecoinEUORG/EuropecoinV2",
        'services': {
            'current_price': {
                'btc': [Bittrex],
                '*': [Cryptonator],
            },
            'address_balance': [],
            'historical_transactions': [],
            'single_transaction': [],
            'push_tx': [],
            'unspent_outputs': [],
            'get_block': []
        },
    },

    'tx': {
        'name': 'TransferCoin',
        'address_version_byte': 66,
        'bip44_coin_type': None,
        'private_key_prefix': 153,
        'message_magic': b"\xd1\x2e\x1e\xe6",
        'genesis_date': datetime(1, 1, 1),
        'github_link': "https://github.com/transferdev/Transfercoin",
        'services': {
            'current_price': {
                'btc': [Bittrex, YoBit, Cryptopia], 'ltc': [Cryptopia],
                'doge': [Cryptopia], 'uno': [Cryptopia], '*': [Cryptonator]
            },
            'address_balance': [CryptoID],
            'historical_transactions': [],
            'single_transaction': [CryptoID],
            'push_tx': [],
            'unspent_outputs': [CryptoID],
            'get_block': []
        },
    },

    'maid': {
        'name': 'MaidSafeCoin',
        'address_version_byte': 0,
        'bip44_coin_type': None,
        'private_key_prefix': None,
        'genesis_date': datetime(1, 1, 1),
        'services': {
            'current_price': {
                'btc': [Bittrex, Poloniex, Cryptopia], 'ltc': [Cryptopia],
                'doge': [Cryptopia], 'uno': [Cryptopia], '*': [Cryptonator]
            },
            'address_balance': [],
            'historical_transactions': [],
            'single_transaction': [],
            'push_tx': [],
            'unspent_outputs': [],
            'get_block': []
        },
    },

    'tips': {
        'name': 'FedoraCoin',
        'address_version_byte': 33,
        'bip44_coin_type': None,
        'private_key_prefix': 161   ,
        'genesis_date': datetime(2013, 12, 21),
        'github_link': "https://github.com/fedoracoin/fedoracoin",
        'services': {
            'current_price': {
                'ltc': [BTER, NovaExchange], 'moon': [NovaExchange],
                '*': [Cryptonator], 'piggy': [NovaExchange]
            },
            'address_balance': [CryptoID],
            'historical_transactions': [],
            'single_transaction': [CryptoID],
            'push_tx': [],
            'unspent_outputs': [CryptoID],
            'get_block': []
        },
    },

    'karma': {
        'name': 'KarmaCoin',
        'address_version_byte': 45,
        'bip44_coin_type': None,
        'private_key_prefix': 173,
        'genesis_date': datetime(2014, 2, 4),
        'github_link': "https://github.com/karmacoin-team/karmacoin",
        'services': {
            'current_price': {
                'btc': [YoBit],
                '*': [Cryptonator],
            },
            'address_balance': [CryptoID],
            'historical_transactions': [],
            'single_transaction': [CryptoID],
            'push_tx': [],
            'unspent_outputs': [CryptoID],
            'get_block': []
        },
    },

    'flap': {
        'name': 'FlappyCoin',
        'address_version_byte': 35,
        'bip44_coin_type': None,
        'private_key_prefix': 163,
        'genesis_date': datetime(2014, 2, 14),
        'github_link': "https://github.com/flappycoin-project/flappycoin",
        'services': {
            'current_price': {},
            'address_balance': [CryptoID],
            'historical_transactions': [],
            'single_transaction': [CryptoID],
            'push_tx': [],
            'unspent_outputs': [CryptoID],
            'get_block': []
        },
    },

    'pot': {
        'name': 'PotCoin',
        'address_version_byte': 55,
        'bip44_coin_type': 0x80000051,
        'private_key_prefix': 183,
        'genesis_date': datetime(2014, 1, 21),
        'github_link': "https://github.com/potcoin/Potcoin",
        'supply_data': {
            'method': 'standard',
            'start_coins_per_block': 420,
            'minutes_per_block': 0.666666666,
            'full_cap': 420000000,
            'blocks_per_era': 210000
        },
        'services': {
            'current_price': {
                'btc': [Bittrex, Cryptopia, BleuTrade], 'ltc': [Cryptopia],
                'doge': [Cryptopia, BleuTrade], 'uno': [Cryptopia], '*': [Cryptonator],
            },
            'address_balance': [CryptoID, ProHashing],
            'historical_transactions': [ProHashing],
            'single_transaction': [CryptoID],
            'push_tx': [],
            'unspent_outputs': [CryptoID],
            'get_block': [ProHashing]
        },
    },

    'bqc': {
        'name': 'BBQcoin',
        'address_version_byte': 85,
        'bip44_coin_type': None,
        'private_key_prefix': 213,
        'genesis_date': datetime(2012, 7, 15),
        'services': {
            'current_price': {
                '*': [Cryptonator],
            },
            'address_balance': [],
            'historical_transactions': [],
            'single_transaction': [],
            'push_tx': [],
            'unspent_outputs': [],
            'get_block': []
        },
    },

    'nvc': {
        'name': 'Novacoin',
        'address_version_byte': 8,
        'bip44_coin_type': 0x80000032,
        'private_key_prefix': 136,
        'genesis_date': datetime(2012, 10, 1),
        'services': {
            'current_price': {
                'btc': [YoBit, Cryptopia, BleuTrade], 'ltc': [Cryptopia],
                'doge': [Cryptopia, BleuTrade], '*': [Cryptonator],
            },
            'address_balance': [CryptapUS, Bchain],
            'historical_transactions': [],
            'single_transaction': [],
            'push_tx': [],
            'unspent_outputs': [],
            'get_block': []
        },
    },

    'uno': {
        'name': 'Unobtanium',
        'address_version_byte': 130,
        'bip44_coin_type': 0x8000005c,
        'private_key_prefix': 224,
        'genesis_date': datetime(2013, 10, 17),
        'supply_data': {
            'method': 'standard',
            'full_cap': 250000,
            'blocks_per_era': 100000,
            'minutes_per_block': 3,
        },
        'services': {
            'current_price': {
                'btc': [Bittrex, CexIO, Cryptopia, BleuTrade], 'ltc': [Cryptopia],
                'usd': [CexIO, Cryptopia], 'doge': [Cryptopia, BleuTrade],
                '*': [Cryptonator],
            },
            'address_balance': [UNOCryptap, CryptoID],
            'historical_transactions': [UNOCryptap, CryptoID],
            'single_transaction': [UNOCryptap],
            'push_tx': [UNOCryptap],
            'unspent_outputs': [UNOCryptap, CryptoID],
            'get_block': [UNOCryptap]
        },
    },

    'ric': {
        'name': 'Riecoin',
        'address_version_byte': 60,
        'bip44_coin_type': 0x8000008f,
        'private_key_prefix': 128,
        'genesis_date': datetime(2014, 2, 11, 0, 49, 1),
        'supply_data': {
            'method': 'standard',
            'start_coins_per_block': 50,
            'minutes_per_block': 2.5,
            'blocks_per_era': 840000,
        },
        'services': {
            'current_price': {
                'btc': [Poloniex], 'cny': [BTC38],
                '*': [Cryptonator],
            },
            'address_balance': [RICCryptap, Bchain, CryptoID],
            'historical_transactions': [RICCryptap],
            'single_transaction': [RICCryptap, CryptoID],
            'push_tx': [RICCryptap],
            'unspent_outputs': [RICCryptap, CryptoID],
            'get_block': [RICCryptap]
        },
    },

    'xrp': {
        'name': 'Ripple',
        'genesis_date': datetime(2011, 3, 1),
        'bip44_coin_type': 0x80000090,
        'services': {
            'current_price': {
                'btc': [Bittrex, Bitstamp, Poloniex, Bitso, BitcoinIndonesia, Kraken],
                'cad': [Kraken], 'usd': [Bitstamp, Kraken, xBTCe], 'cny': [BTC38],
                'eur': [Bitstamp, Kraken, xBTCe], 'jpy': [Kraken], 'mxn': [Bitso],
                'krw': [CoinOne], '*': [Cryptonator],
            },
        }
    },

    'thc': {
        'name': 'HempCoin',
        'address_version_byte': 40,
        'bip44_coin_type': None,
        'private_key_prefix': 168,
        'genesis_date': datetime(1, 1, 1),
        'github_link': "https://github.com/hempcoin-project/THC",
        'supply_data': {
            'method': 'standard',
            'start_coins_per_block': None,
            'minutes_per_block': 1.0,
            'full_cap': None,
            'blocks_per_era': None,
            'reward_ends_at_block': None
        },
        'services': {
            'current_price': {
                'btc': [Bittrex], '*': [Cryptonator],
            },
            'address_balance': [BlockExperts],
            'historical_transactions': [],
            'single_transaction': [BlockExperts],
            'push_tx': [],
            'unspent_outputs': [],
            'get_block': [BlockExperts]
        },
    },

    'dope': {
        'name': 'Dopecoin',
        'address_version_byte': 8,
        'bip44_coin_type': None,
        'private_key_prefix': None,
        'genesis_date': datetime(1, 1, 1),
        'services': {
            'current_price': {
                'btc': [Bittrex, Cryptonator],
                '*': [Cryptonator],
            },
            'address_balance': [BlockExperts],
            'historical_transactions': [],
            'single_transaction': [BlockExperts],
            'push_tx': [],
            'unspent_outputs': [],
            'get_block': [BlockExperts]
        },
    },

    'dime': {
        'name': 'Dimecoin',
        'address_version_byte': 15,
        'bip44_coin_type': None,
        'private_key_prefix': None,
        'genesis_date': datetime(2014, 12, 23),
        'services': {
            'current_price': {
                'btc': [YoBit, Cryptonator], 'doge': [Cryptopia],
                'ltc': [Cryptopia], 'uno': [Cryptopia],
                '*': [Cryptonator],
            },
            'address_balance': [BlockExperts],
            'historical_transactions': [],
            'single_transaction': [BlockExperts],
            'push_tx': [],
            'unspent_outputs': [],
            'get_block': [BlockExperts]
        },
    },

    'xcp': {
        'name': 'CounterParty',
        'address_version_byte': 0,
        'bip44_coin_type': 0x80000009,
        'private_key_prefix': 128,
        'genesis_date': datetime(2014, 1, 2),
        'services': {
            'current_price': {
                'btc': [Bittrex, Poloniex, Cryptonator],
                '*': [Cryptonator],
            },
            'address_balance': [CoinDaddy1, CoinDaddy2, CounterPartyChain],
            'historical_transactions': [CoinDaddy1, CoinDaddy2],
            'single_transaction': [CoinDaddy1, CoinDaddy2],
            'push_tx': [CoinDaddy1, CoinDaddy2],
            'unspent_outputs': [CoinDaddy1],
            'get_block': [CoinDaddy1, CoinDaddy2]
        },
    },

    'eth': {
        'name': 'Ethereum',
        'address_version_byte': None,
        'address_encoding': "hex",
        'bip44_coin_type': 0x8000003c,
        'private_key_prefix': None,
        'genesis_date': datetime(2015, 7, 30),
        'supply_data': {
            'instamine': 72009990.50
        },
        'services': {
            'current_price': {
                'rur': [YoBit, xBTCe], 'usd': [GDAX, Kraken, xBTCe, Liqui], 'cny': [Yunbi, xBTCe],
                'jpy': [Kraken, xBTCe], 'eur': [xBTCe, Kraken], 'cad': [Kraken],
                'gbp': [Kraken], 'mxn': [Bitso], 'krw': [CoinOne],
                'btc': [
                    Poloniex, GDAX, Kraken, xBTCe, BleuTrade, Bittrex, CexIO,
                    BitcoinIndonesia, EtherChain, YoBit, Cryptopia, Bitso, Liqui
                ],
                'ltc': [Cryptopia, xBTCe], 'doge': [Cryptopia, BleuTrade], 'uno': [Cryptopia],
                '*': [Cryptonator],
            },
            'address_balance': [Etherscan, EtherChain, ETCchain],
            'historical_transactions': [],
            'single_transaction': [],
            'push_tx': [],
            'unspent_outputs': [],
            'get_block': []
        },
    },

    'etc': {
        'name': 'Ethereum Classic',
        'address_version_byte': None,
        'address_encoding': "hex",
        'bip44_coin_type': 0x8000003d,
        'private_key_prefix': None,
        'genesis_date': datetime(2016, 7, 20),
        'services': {
            'current_price': {
                'btc': [Poloniex, Bittrex, CexIO, Kraken, Cryptopia, YoBit, Yunbi],
                'usd': [Kraken, CexIO], 'doge': [Cryptopia], 'eur': [Kraken],
                'ltc': [CexIO, Cryptopia], 'uno': [Cryptopia], 'krw': [CoinOne],
                '*': [Cryptonator], 'eth': [Kraken]
            },
            'address_balance': [ETCchain],
            'historical_transactions': [],
            'single_transaction': [],
            'push_tx': [],
            'unspent_outputs': [],
            'get_block': []
        },
    },

    'xmr': {
        'name': 'Monero',
        'address_version_byte': None,
        'bip44_coin_type': 0x80000080,
        'private_key_prefix': None,
        'genesis_date': datetime(2014, 4, 18),
        'services': {
            'current_price': {
                'btc': [Poloniex, Bittrex, Kraken, Cryptopia], 'ltc': [Cryptopia],
                'doge': [Cryptopia], 'uno': [Cryptopia], 'usd': [Kraken, Cryptopia],
                'nzd': [Cryptopia], 'eur': [Kraken], '*': [Cryptonator],
            },
            'address_balance': [],
            'historical_transactions': [],
            'single_transaction': [],
            'push_tx': [],
            'unspent_outputs': [],
            'get_block': []
        }
    },

    'blk': {
        'name': 'Blackcoin',
        'message_magic': b"\x70\x35\x22\x05",
        'address_version_byte': 25,
        'bip44_coin_type': 0x8000000a,
        'private_key_prefix': 153,
        'genesis_date': datetime(1, 1, 1),
        'services': {
            'current_price': {
                'btc': [Poloniex, Cryptopia, UseCryptos, BleuTrade], 'ltc': [Cryptopia],
                'doge': [Cryptopia, BleuTrade], 'uno': [Cryptopia],
                '*': [Cryptonator], 'cny': [BTC38],
            },
            'address_balance': [
                HolyTransaction, Bchain
            ],
            'historical_transactions': [],
            'single_transaction': [],
            'push_tx': [],
            'unspent_outputs': [],
            'get_block': []
        },
    },

    'xpm': {
        'name': 'Primecoin',
        'address_version_byte': 23,
        'bip44_coin_type': 0x80000018,
        'private_key_prefix': 151,
        'genesis_date': datetime(1, 1, 1),
        'services': {
            'current_price': {
                'btc': [Poloniex, Cryptopia, Vircurex, BleuTrade], 'ltc': [Cryptopia],
                'doge': [Cryptopia, BleuTrade], 'uno': [Cryptopia],
                'cny': [BTC38],
                '*': [Cryptonator],
            },
            'address_balance': [
                Bchain
            ],
            'historical_transactions': [],
            'single_transaction': [],
            'push_tx': [],
            'unspent_outputs': [],
            'get_block': []
        },
    },

    'pivx': {
        'name': 'PivX',
        'address_version_byte': 30,
        'bip44_coin_type': 0x80000077,
        'private_key_prefix': 212,
        'genesis_date': datetime(1, 1, 1),
        'services': {
            'current_price': {
                'btc': [Bittrex, Cryptopia, YoBit], 'usd': [Cryptopia],
                'ltc': [Cryptopia], 'doge': [Cryptopia], 'uno': [Cryptopia],
                '*': [Cryptonator],
            },
            'address_balance': [PressTab, CryptoID],
            'historical_transactions': [],
            'single_transaction': [CryptoID],
            'push_tx': [],
            'unspent_outputs': [CryptoID],
            'get_block': []
        },
    },
    'zec': {
        'name': 'ZCash',
        'address_version_byte': 7352,
        'bip44_coin_type': 0x80000085,
        'private_key_prefix': 128,
        'genesis_date': datetime(2016, 10, 28, 7, 56),
        'message_magic': b"\x24\xe9\x27\x64",
        'github_link': "https://github.com/zcash/zcash",
        'services': {
            'current_price': {
                'btc': [Bittrex, YoBit, Kraken], 'usd': [Kraken], 'eur': [Kraken],
                '*': [Cryptonator],
            },
            'address_balance': [ZChain, MercerWeiss],
            'historical_transactions': [MercerWeiss],
            'single_transaction': [MercerWeiss],
            'push_tx': [MercerWeiss],
            'unspent_outputs': [MercerWeiss],
            'get_block': [MercerWeiss]
        },
    },
    'grs': {
        'name': 'Groestlcoin',
        'address_version_byte': 36,
        "address_encoding": "groestlbase58",
        'bip44_coin_type': 0x80000011,
        'private_key_prefix': 128,
        'message_magic': b"\xF9\xBE\xB4\xD4",
        'genesis_date': datetime(1, 1, 1),
        'services': {
            'current_price': {
                'btc': [Bittrex],
                '*': [Cryptonator],
            },
            'address_balance': [CryptoID],
            'historical_transactions': [],
            'single_transaction': [CryptoID],
            'push_tx': [],
            'unspent_outputs': [CryptoID],
            'get_block': []
        },
    },
    'sys': {
        'name': 'Syscoin 2.1',
        'address_version_byte': 0,
        'bip44_coin_type': 0x80000039,
        'private_key_prefix': 128,
        'genesis_date': datetime(1, 1, 1),
        'services': {
            'current_price': {
                'btc': [Bittrex, YoBit, BTC38],
                '*': [Cryptonator],
            },
            'address_balance': [ProHashing, CryptoID],
            'historical_transactions': [],
            'single_transaction': [CryptoID],
            'push_tx': [],
            'unspent_outputs': [CryptoID],
            'get_block': []
        },
    },
    'bun': {
        'name': 'BunnyCoin',
        'address_version_byte': 26,
        'bip44_coin_type': None,
        'private_key_prefix': 154,
        'genesis_date': datetime(2014, 4, 25, 16, 0),
        'services': {
            'current_price': {
                'ltc': [Cryptopia, NovaExchange], 'moon': [NovaExchange],
                'doge': [Cryptopia, NovaExchange], 'uno': [Cryptopia],
            },
            'address_balance': [ProHashing, CryptoChat],
            'historical_transactions': [CryptoChat],
            'single_transaction': [CryptoChat],
            'push_tx': [],
            'unspent_outputs': [],
            'get_block': [CryptoChat]
        },
    },
    'bvc': {
        'name': 'BeaverCoin',
        'address_version_byte': 25,
        'bip44_coin_type': None,
        'private_key_prefix': 176,
        'genesis_date': datetime(1, 1, 1),
        'supply_data': {
            'method': 'standard',
            'start_coins_per_block': 8,
            'minutes_per_block': 1,
            'full_cap': 3360000,
            'blocks_per_era': 210000,
            'reward_ends_at_block': None
        },
        'services': {
            'current_price': {
                'btc': [Cryptopia], 'ltc': [Cryptopia], 'doge': [Cryptopia],
                'uno': [Cryptopia],
            },
            'address_balance': [ProHashing, BeavercoinBlockchain],
            'historical_transactions': [BeavercoinBlockchain],
            'single_transaction': [BeavercoinBlockchain],
            'push_tx': [BeavercoinBlockchain],
            'unspent_outputs': [BeavercoinBlockchain],
            'get_block': [BeavercoinBlockchain]
        },
    },
    'cat': {
        'name': 'Catcoin',
        'address_version_byte': 21,
        'bip44_coin_type': None,
        'private_key_prefix': 149,
        'message_magic': None,
        'genesis_date': datetime(1, 1, 1),
        'supply_data': {
            'method': 'standard',
            'start_coins_per_block': 50,
            'minutes_per_block': 10,
            'full_cap': 21000000,
            'blocks_per_era': 210000,
            'reward_ends_at_block': None
        },
        'services': {
            'current_price': {},
            'address_balance': [],
            'historical_transactions': [],
            'single_transaction': [],
            'push_tx': [],
            'unspent_outputs': [],
            'get_block': []
        },
    },
    'lemon': {
        'name': 'LemonCoin',
        'address_version_byte': 48,
        'bip44_coin_type': None,
        'private_key_prefix': 176,
        'message_magic': None,
        'genesis_date': datetime(1, 1, 1),
        'supply_data': {
            'method': 'standard',
            'start_coins_per_block': 20,
            'minutes_per_block': 1,
            'full_cap': 31000000,
            'blocks_per_era': 525000,
            'reward_ends_at_block': None,
            'ico': 10000000,
            'ico_burn': 8960948,
        },
        'services': {
            'current_price': {
                'btc': [Cryptopia], 'ltc': [Cryptopia], 'doge': [Cryptopia],
                'uno': [Cryptopia],
            },
            'address_balance': [LemoncoinOfficial],
            'historical_transactions': [LemoncoinOfficial],
            'single_transaction': [LemoncoinOfficial],
            'push_tx': [],
            'unspent_outputs': [],
            'get_block': [LemoncoinOfficial]
        },
    },
    'geert': {
        'name': 'Geertcoin',
        'address_version_byte': 38,
        'bip44_coin_type': None,
        'private_key_prefix': None,
        'message_magic': None,
        'genesis_date': datetime(2017, 2, 12, 6, 25, 23),
        'supply_data': {
            'method': 'standard',
            'start_coins_per_block': 200,
            'minutes_per_block': 2.5,
            'full_cap': None,
            'blocks_per_era': 24000,
            'reward_ends_at_block': None
        },
        'services': {
            'current_price': {
                'btc': [Cryptopia], 'ltc': [Cryptopia], 'doge': [Cryptopia]
            },
            'address_balance': [GeertcoinExplorer],
            'historical_transactions': [GeertcoinExplorer],
            'single_transaction': [GeertcoinExplorer],
            'push_tx': [],
            'unspent_outputs': [],
            'get_block': [GeertcoinExplorer]
        },
    },
    'ulm': {
        'name': 'UnlimitedCoin',
        'address_version_byte': 68,
        'bip44_coin_type': None,
        'private_key_prefix': None,
        'message_magic': None,
        'genesis_date': datetime(2017, 5, 19, 17, 55, 39),
        'supply_data': {
            'method': 'standard',
            'start_coins_per_block': None,
            'minutes_per_block': None,
            'full_cap': None,
            'blocks_per_era': None,
            'reward_ends_at_block': None
        },
        'services': {
            'current_price': {'btc': [NovaExchange]},
            'address_balance': [UnlimitedCoinOfficial],
            'historical_transactions': [UnlimitedCoinOfficial],
            'single_transaction': [UnlimitedCoinOfficial],
            'push_tx': [],
            'unspent_outputs': [],
            'get_block': [UnlimitedCoinOfficial]
        },
    },
    'mrs': {
        'name': 'MarsCoin',
        'address_version_byte': 50,
        'bip44_coin_type': 0x8000006b,
        'private_key_prefix': 178,
        'message_magic': None,
        'genesis_date': datetime(2014, 1, 1, 15, 37, 7),
        'supply_data': {
            'method': 'standard',
            'start_coins_per_block': 50,
            'minutes_per_block': None,
            'full_cap': None,
            'blocks_per_era': None,
            'reward_ends_at_block': None
        },
        'services': {
            'current_price': {'btc': [NovaExchange]},
            'address_balance': [MarscoinOfficial],
            'historical_transactions': [MarscoinOfficial],
            'single_transaction': [MarscoinOfficial],
            'push_tx': [MarscoinOfficial],
            'unspent_outputs': [MarscoinOfficial],
            'get_block': [MarscoinOfficial]
        },
    },
    'moon': {
        'name': 'Mooncoin',
        'address_version_byte': 3,
        'bip44_coin_type': None,
        'private_key_prefix': 131,
        'message_magic': None,
        'genesis_date': datetime(1, 1, 1),
        'supply_data': {
            'method': 'standard',
            'start_coins_per_block': None,
            'minutes_per_block': 1.5,
            'full_cap': None,
            'blocks_per_era': None,
            'reward_ends_at_block': None
        },
        'services': {
            'current_price': {
                'btc': [CexIO, NovaExchange, BleuTrade], 'usd': [CexIO],
                'ltc': [CexIO, NovaExchange, BleuTrade], 'doge': [CexIO]
            },
            'address_balance': [ProHashing, Bchain],
            'historical_transactions': [],
            'single_transaction': [],
            'push_tx': [],
            'unspent_outputs': [],
            'get_block': []
        },
    },
    'rby': {
        'name': 'Rubycoin',
        'address_version_byte': 60,
        'bip44_coin_type': 0x80000010,
        'private_key_prefix': 188,
        'message_magic': None,
        'genesis_date': datetime(1, 1, 1),
        'supply_data': {
            'method': 'standard',
            'start_coins_per_block': None,
            'minutes_per_block': 1.5,
            'full_cap': None,
            'blocks_per_era': None,
            'reward_ends_at_block': None
        },
        'services': {
            'current_price': {
                'btc': [Bittrex, Cryptopia], 'ltc': [Cryptopia],
                'doge': [Cryptopia], 'uno': [Cryptopia]
            },
            'address_balance': [CryptoID],
            'historical_transactions': [],
            'single_transaction': [CryptoID],
            'push_tx': [],
            'unspent_outputs': [CryptoID],
            'get_block': []
        },
    },
    'pnd': {
        'name': 'PandaCoin',
        'address_version_byte': 55,
        'bip44_coin_type': 0x80000025,
        'private_key_prefix': 183,
        'message_magic': None,
        'genesis_date': datetime(1, 1, 1),
        'supply_data': {
            'method': 'standard',
            'start_coins_per_block': None,
            'minutes_per_block': 1.0,
            'full_cap': None,
            'blocks_per_era': None,
            'reward_ends_at_block': None
        },
        'services': {
            'current_price': {
                'btc': [YoBit], 'ltc': [Cryptopia],
                'doge': [Cryptopia], 'uno': [Cryptopia]
            },
            'address_balance': [CryptoID],
            'historical_transactions': [],
            'single_transaction': [CryptoID],
            'push_tx': [],
            'unspent_outputs': [CryptoID],
            'get_block': []
        },
    },
    'trc': {
        'name': 'TerraCoin',
        'address_version_byte': 0,
        'bip44_coin_type': 0x80000053,
        'private_key_prefix': 128,
        'message_magic': b"\x42\xba\xbe\x56",
        'genesis_date': datetime(1, 1, 1),
        'github_link': "https://github.com/clockuniverse/terracoin",
        'supply_data': {
            'method': 'standard',
            'start_coins_per_block': 20,
            'minutes_per_block': 2,
            'full_cap': None,
            'blocks_per_era': 1050000,
            'reward_ends_at_block': None
        },
        'services': {
            'current_price': {
                'btc': [CexIO, Vircurex, Cryptopia], 'usd': [CexIO, Vircurex],
                'ltc': [CexIO, Cryptopia, NovaExchange],
                'doge': [CexIO, Cryptopia, NovaExchange]
            },
            'address_balance': [TRCPress],
            'historical_transactions': [],
            'single_transaction': [],
            'push_tx': [],
            'unspent_outputs': [],
            'get_block': []
        },
    },
    'dgc': {
        'name': 'DigitalCoin',
        'address_version_byte': 30,
        'bip44_coin_type': 0x80000012,
        'private_key_prefix': 158,
        'message_magic': b"\xfb\xc0\xb6\xdb",
        'genesis_date': datetime(1, 1, 1),
        'github_link': "https://github.com/DGCDev/digitalcoin",
        'supply_data': {
            'method': 'standard',
            'start_coins_per_block': None,
            'minutes_per_block': 0.666666666,
            'full_cap': None,
            'blocks_per_era': None,
            'reward_ends_at_block': None
        },
        'services': {
            'current_price': {
                'btc': [BleuTrade, NovaExchange, Cryptopia, Vircurex],
                'usd': [Vircurex], 'eur': [Vircurex], 'cny': [BTC38],
                'ltc': [Cryptopia, NovaExchange, Vircurex],
                'doge': [Vircurex, BleuTrade, Cryptopia, NovaExchange]
            },
            'address_balance': [CryptoID],
            'historical_transactions': [],
            'single_transaction': [CryptoID],
            'push_tx': [],
            'unspent_outputs': [CryptoID],
            'get_block': []
        },
    },
    'qrk': {
        'name': 'Quark',
        'address_version_byte': 58,
        'bip44_coin_type': None,
        'private_key_prefix': 186,
        'message_magic': None,
        'genesis_date': datetime(1, 1, 1),
        'supply_data': {
            'method': 'standard',
            'start_coins_per_block': None,
            'minutes_per_block': None,
            'full_cap': None,
            'blocks_per_era': None,
            'reward_ends_at_block': None
        },
        'services': {
            'current_price': {
                'btc': [NovaExchange, Vircurex, Cryptopia, BTC38],
                'ltc': [Vircurex, NovaExchange, Cryptopia], 'eur': [Vircurex],
                'usd': [Vircurex], 'doge': [Cryptopia, NovaExchange],
            },
            'address_balance': [CryptoID],
            'historical_transactions': [],
            'single_transaction': [CryptoID],
            'push_tx': [],
            'unspent_outputs': [CryptoID],
            'get_block': []
        },
    },
    'tse': {
        'name': 'Tattoocoin',
        'address_version_byte': 65,
        'bip44_coin_type': None,
        'private_key_prefix': 193,
        'message_magic': None,
        'genesis_date': datetime(2016, 12, 29, 21, 53, 10),
        'github_link': 'https://github.com/CryptoCoderz/Tattoocoin-TSE',
        'supply_data': {
            'method': 'standard',
            'start_coins_per_block': None,
            'minutes_per_block': None,
            'full_cap': None,
            'blocks_per_era': None,
            'reward_ends_at_block': None
        },
        'services': {
            'current_price': {
                'btc': [YoBit, CexIO, NovaExchange, Cryptopia],
                'ltc': [CexIO, NovaExchange, Cryptopia], 'usd': [CexIO],
                'doge': [CexIO, Cryptopia],
            },
            'address_balance': [CryptoChat],
            'historical_transactions': [CryptoChat],
            'single_transaction': [CryptoChat],
            'push_tx': [],
            'unspent_outputs': [],
            'get_block': [CryptoChat]
        },
    },
    'xvg': {
        'name': 'Verge',
        'address_version_byte': 30,
        'bip44_coin_type': 0x8000004d,
        'private_key_prefix': 158,
        'message_magic': None,
        'genesis_date': datetime(2014, 10, 9, 18, 22, 44),
        'github_link': "https://github.com/vergecurrency/VERGE",
        'supply_data': {
            'method': 'standard',
            'start_coins_per_block': None,
            'minutes_per_block': 0.5,
            'full_cap': None,
            'blocks_per_era': None,
            'reward_ends_at_block': None
        },
        'services': {
            'current_price': {
                'btc': [YoBit, CexIO, Bittrex, Cryptopia, NovaExchange],
                'ltc': [CexIO, Cryptopia, NovaExchange], 'usd': [CexIO],
                'doge': [CexIO, NovaExchange, Cryptopia]
            },
            'address_balance': [VergeCurrencyInfo, ProHashing],
            'historical_transactions': [VergeCurrencyInfo],
            'single_transaction': [VergeCurrencyInfo],
            'push_tx': [],
            'unspent_outputs': [],
            'get_block': [VergeCurrencyInfo]
        },
    },
    '1337': {
        'name': '1337',
        'address_version_byte': 48,
        'bip44_coin_type': None,
        'private_key_prefix': 176,
        'message_magic': None,
        'genesis_date': datetime(1, 1, 1),
        'github_link': 'https://github.com/Velvet78/1337',
        'supply_data': {
            'method': 'standard',
            'start_coins_per_block': None,
            'minutes_per_block': None,
            'full_cap': None,
            'blocks_per_era': None,
            'reward_ends_at_block': None
        },
        'services': {
            'current_price': {
                'btc': [YoBit, Cryptopia, NovaExchange],
                'ltc': [Cryptopia, NovaExchange], 'moon': [NovaExchange],
                'doge': [Cryptopia, NovaExchange],
            },
            'address_balance': [CryptoID],
            'historical_transactions': [],
            'single_transaction': [CryptoID],
            'push_tx': [],
            'unspent_outputs': [CryptoID],
            'get_block': [],
            "get_optimal_fee": []
        },
    },
    'cj': {
        'name': 'CryptoJacks',
        'address_version_byte': 28,
        'bip44_coin_type': None,
        'private_key_prefix': 156,
        'message_magic': None,
        'genesis_date': datetime(1, 1, 1),
        'github_link': "https://github.com/cryptojacks/CryptoJacks",
        'supply_data': {
            'method': 'standard',
            'start_coins_per_block': None,
            'minutes_per_block': None,
            'full_cap': None,
            'blocks_per_era': None,
            'reward_ends_at_block': None
        },
        'services': {
            'current_price': {
                'btc': [CexIO, NovaExchange, Cryptopia, YoBit],
                'ltc': [CexIO, NovaExchange, Cryptopia], 'usd': [CexIO],
                'doge': [Cryptopia, NovaExchange]
            },
            'address_balance': [],
            'historical_transactions': [],
            'single_transaction': [],
            'push_tx': [],
            'unspent_outputs': [],
            'get_block': [],
            "get_optimal_fee": []
        },
    },
    'fjc': {
        'name': 'FujiCoin',
        'address_version_byte': 36,
        'bip44_coin_type': 0x8000004b,
        'private_key_prefix': 164,
        'message_magic': None,
        'genesis_date': datetime(2014, 6, 27, 23, 0),
        'github_link': "https://github.com/fujicoin/fujicoin",
        'supply_data': {
            'method': 'standard',
            'start_coins_per_block': None,
            'minutes_per_block': 1,
            'full_cap': None,
            'blocks_per_era': None,
            'reward_ends_at_block': None
        },
        'services': {
            'current_price': {
                'btc': [YoBit, CexIO, NovaExchange, Cryptopia, BleuTrade],
                'ltc': [CexIO, Cryptopia, NovaExchange], 'usd': [CexIO],
                'doge': [CexIO, NovaExchange, Cryptopia]
            },
            'address_balance': [FujiInsght],
            'historical_transactions': [FujiInsght],
            'single_transaction': [FujiInsght],
            'push_tx': [FujiInsght],
            'unspent_outputs': [FujiInsght],
            'get_block': [FujiInsght],
            "get_optimal_fee": []
        },
    },
    'note': {
        'name': 'DNotes',
        'address_version_byte': 31,
        'bip44_coin_type': None,
        'private_key_prefix': 159,
        'message_magic': None,
        'genesis_date': datetime(1, 1, 1),
        'github_link': "https://github.com/DNotesCoin/DNotes/",
        'supply_data': {
            'method': 'standard',
            'start_coins_per_block': None,
            'minutes_per_block': 1,
            'full_cap': None,
            'blocks_per_era': None,
            'reward_ends_at_block': None
        },
        'services': {
            'current_price': {
                'btc': [YoBit, CexIO, Poloniex, NovaExchange, Cryptopia],
                'ltc': [CexIO, Cryptopia, NovaExchange], 'usd': [CexIO],
                'doge': [CexIO, NovaExchange, Cryptopia]
            },
            'address_balance': [CryptoID, ProHashing],
            'historical_transactions': [],
            'single_transaction': [CryptoID],
            'push_tx': [],
            'unspent_outputs': [CryptoID],
            'get_block': [],
            "get_optimal_fee": []
        },
    },
    'song': {
        'name': 'SongCoin',
        'address_version_byte': 63,
        'bip44_coin_type': None,
        'private_key_prefix': 191,
        'message_magic': None,
        'genesis_date': datetime(1, 1, 1),
        'github_link': "https://github.com/Songcoin/Songcoin",
        'supply_data': {
            'method': 'standard',
            'start_coins_per_block': None,
            'minutes_per_block': 2,
            'full_cap': None,
            'blocks_per_era': None,
            'reward_ends_at_block': None
        },
        'services': {
            'current_price': {
                'btc': [YoBit, CexIO, NovaExchange, Cryptopia],
                'ltc': [CexIO, Cryptopia], 'usd': [CexIO],
                'doge': [CexIO, NovaExchange, Cryptopia]
            },
            'address_balance': [ProHashing],
            'historical_transactions': [],
            'single_transaction': [],
            'push_tx': [],
            'unspent_outputs': [],
            'get_block': [],
            'get_optimal_fee': []
        },
    },
    'ptc': {
        'name': 'Pesetacoin',
        'address_version_byte': 47,
        'bip44_coin_type': None,
        'private_key_prefix': 175,
        'message_magic': b"\xc0\xc0\xc0\xc0",
        'genesis_date': datetime(2013, 12, 31, 22, 23, 8),
        'github_link': "https://github.com/pesetachain/pesetacoin-0.9",
        'supply_data': {
            'method': 'per_era',
            'eras': [
                {'start': 0,      'end': 525600, 'reward': 166.386},
                {'start': 525601, 'end': 550000, 'reward': 83.193},
                {'start': 550001, 'end': 1051200, 'reward': 50},
                {'start': 1051201, 'end': 1576800, 'reward': 25},
                {'start': 1576801, 'end': 2628000, 'reward': 10},
                {'start': 2628001, 'end': 8409600, 'reward': 5},
                {'start': 8409601, 'end': None, 'reward': 0},
            ],
            'full_cap': 166386000,
            'reward_ends_at_block': 8409601
        },
        'services': {
            'current_price': {
                'btc': [Bittrex, Cryptopia, NovaExchange], 'ltc': [Cryptopia],
                'uno': [Cryptopia], 'doge': [Cryptopia]
            },
            'address_balance': [PesetacoinInfo, CryptoID, PresetacoinInsight],
            'historical_transactions': [PesetacoinInfo, PresetacoinInsight],
            'single_transaction': [PesetacoinInfo, CryptoID, PresetacoinInsight],
            'push_tx': [PresetacoinInsight],
            'unspent_outputs': [PesetacoinInfo, CryptoID, PresetacoinInsight],
            'get_block': [PesetacoinInfo],
            'get_optimal_fee': []
        },
    },
    'tes': {
        'name': 'TeslaCoin',
        'address_version_byte': 11,
        'bip44_coin_type': None,
        'private_key_prefix': 139,
        'message_magic': None,
        'genesis_date': datetime(1, 1, 1),
        'github_link': "https://github.com/TeslacoinFoundation/Teslacoin",
        'supply_data': {
            'method': 'standard',
            'start_coins_per_block': None,
            'minutes_per_block': None,
            'full_cap': None,
            'blocks_per_era': None,
            'reward_ends_at_block': None
        },
        'services': {
            'current_price': {
                'btc': [YoBit, Cryptopia, NovaExchange], 'ltc': [Cryptopia, NovaExchange],
                'uno': [Cryptopia], 'doge': [Cryptopia, NovaExchange]
            },
            'address_balance': [CryptoID],
            'historical_transactions': [],
            'single_transaction': [CryptoID],
            'push_tx': [],
            'unspent_outputs': [CryptoID],
            'get_block': [],
            'get_optimal_fee': []
        },
    },
    'xvc': {
        'name': 'Vcash',
        'address_version_byte': 71,
        'bip44_coin_type': None,
        'private_key_prefix': 199,
        'message_magic': None,
        'genesis_date': datetime(1, 1, 1),
        'github_link': "https://github.com/openvcash/vcash",
        'supply_data': {
            'method': 'standard',
            'start_coins_per_block': None,
            'minutes_per_block': None,
            'full_cap': None,
            'blocks_per_era': None,
            'reward_ends_at_block': None
        },
        'services': {
            'current_price': {
                'btc': [Bittrex, Poloniex]
            },
            'address_balance': [VChainInfo],
            'historical_transactions': [],
            'single_transaction': [VChainInfo],
            'push_tx': [],
            'unspent_outputs': [VChainInfo],
            'get_block': [],
            'get_optimal_fee': []
        },
    },
    'meow': {
        'name': 'KittehCoin',
        'address_version_byte': 45,
        'bip44_coin_type': None,
        'private_key_prefix': 173,
        'message_magic': None,
        'genesis_date': datetime(1, 1, 1),
        'github_link': "https://github.com/kittehcoin/kittehcoin",
        'supply_data': {
            'method': 'standard',
            'start_coins_per_block': None,
            'minutes_per_block': 1.0,
            'full_cap': None,
            'blocks_per_era': None,
            'reward_ends_at_block': None
        },
        'services': {
            'current_price': {
                'ltc': [Cryptopia, NovaExchange], 'doge': [Cryptopia]
            },
            'address_balance': [ProHashing, CryptoID],
            'historical_transactions': [],
            'single_transaction': [CryptoID],
            'push_tx': [],
            'unspent_outputs': [CryptoID],
            'get_block': [],
            'get_optimal_fee': []
        },
    },
    # TEMPLATE
    '': {
        'name': '',
        'address_version_byte': None,
        'bip44_coin_type': None,
        'private_key_prefix': None,
        'message_magic': None,
        'genesis_date': datetime(1, 1, 1),
        'github_link': None,
        'supply_data': {
            'method': 'standard',
            'start_coins_per_block': None,
            'minutes_per_block': None,
            'full_cap': None,
            'blocks_per_era': None,
            'reward_ends_at_block': None
        },
        'services': {
            'current_price': {
                'btc': [], 'ltc': [], 'usd': [], 'doge': []
            },
            'address_balance': [],
            'historical_transactions': [],
            'single_transaction': [],
            'push_tx': [],
            'unspent_outputs': [],
            'get_block': [],
            'get_optimal_fee': []
        },
    },
}
