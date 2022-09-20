from asyncio import constants
from profitability import Profitability
#import requests

#urlERGO = "https://min-api.cryptocompare.com/data/blockchain/mining/calculator?fsyms=ERG&tsyms=USD"

hashrate_ergo = 130000000                   #   Hashes/s
hashrate_raven = 22000000
power_consumption_ergo = 220                #   Watt
power_consumption_raven = 220 

ergo = Profitability('ERG','USD', hashrate_ergo, power_consumption_ergo)
raven = Profitability('RVN','USD', hashrate_raven, power_consumption_raven)

print(ergo.get_price())
print(ergo.get_network_hashrate())
print(ergo.get_block_reward())
print(ergo.get_mined_blocks_per_day())
print(ergo.get_hashrate_share())
print(ergo.get_daily_block_reward())
print(ergo.get_daily_mining_income())
print(raven.get_daily_mining_income())
