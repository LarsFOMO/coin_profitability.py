from asyncio import constants
from profitability import Profitability
import array as arr
import numpy as np
#import requests

#urlERGO = "https://min-api.cryptocompare.com/data/blockchain/mining/calculator?fsyms=ERG&tsyms=USD"

hashrate_ergo = 130000000                   #   Hashes/s
hashrate_raven = 29510000
hashrate_etc = 60210000
hashrate_ethw = 60210000
hashrate_neox = 29510000
hashrate_ae = 8
power_consumption_ergo = 220                #   Watt
power_consumption_raven = 150 
power_consumption_etc = 220
power_consumption_ethw = 220
power_consumption_neox = 150
power_consumption_ae = 122
maxim = 0

ergo = Profitability('ERG','USD', hashrate_ergo, power_consumption_ergo)
raven = Profitability('RVN','USD', hashrate_raven, power_consumption_raven)
etc = Profitability('ETC','USD', hashrate_etc, power_consumption_etc)
ethw = Profitability('ETHW','USD', hashrate_ethw, power_consumption_ethw)
neox = Profitability('NEOX','USD', hashrate_neox, power_consumption_neox)
ae = Profitability('AE','USD', hashrate_ae, power_consumption_ae)

ergoG = ergo.get_daily_mining_income()
ravenG = raven.get_daily_mining_income()
etcG = etc.get_daily_mining_income()
#ethwG = ethw.get_daily_mining_income()
#neoxG = neox.get_daily_mining_income()
aeG = ae.get_daily_mining_income()

namearray = ['ergo','raven','etc','ae']
proarray = [ergoG,ravenG,etcG,aeG]

for i in proarray:
    if(i > maxim):
        maxim = i
        stelle = proarray.index(i)

print('Der Profitabelste Coin ist aktuell:',namearray[stelle])
print(namearray[stelle],"'s täglicher Reward beträgt aktuell:","%.3f" % maxim,'USD')

# print("\nPrice [ERG]: ", ergo.get_price(), "USD")
# print("Network Hashrate: ", ergo.get_network_hashrate())
# print("Block Reward: ",ergo.get_block_reward())
# print("Mined Blocks/Day: ","%.2f" % ergo.get_mined_blocks_per_day())
# print("Hashrate Share: ", ergo.get_hashrate_share())
# print("Daily Block Reward: ", "%.2f" % ergo.get_daily_block_reward())
