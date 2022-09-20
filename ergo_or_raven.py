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

print("\nPrice [ERG]: ", ergo.get_price(), "USD")
print("Network Hashrate: ", ergo.get_network_hashrate())
print("Block Reward: ",ergo.get_block_reward())
print("Mined Blocks/Day: ","%.2f" % ergo.get_mined_blocks_per_day())
print("Hashrate Share: ", ergo.get_hashrate_share())
print("Daily Block Reward: ", "%.2f" % ergo.get_daily_block_reward())

if(ergo.get_daily_mining_income() >= raven.get_daily_mining_income()):
    print("\nErgo (","%.4f" % ergo.get_daily_mining_income(), "USD/Tag) ist aktuell profitabler, zu minen, als Raven (","%.4f" % raven.get_daily_mining_income(), "USD/Tag)\n")
elif(ergo.get_daily_mining_income() < raven.get_daily_mining_income()):
    print("\nRaven (","%.4f" % raven.get_daily_mining_income(), "USD/Tag) ist aktuell profitabler, zu minen, als Ergo (","%.4f" % ergo.get_daily_mining_income(), "USD/Tag)\n")