from profitability import Profitability
import requests

urlERGO = "https://min-api.cryptocompare.com/data/blockchain/mining/calculator?fsyms=ERG&tsyms=USD"

ergo = Profitability('ERG','USD', 130, 220)
raven = Profitability('RVN','USD', 22, 220)

print(ergo.get_price())
print(raven.get_network_hashrate())

print(ergo.get_block_reward())
data = requests.get(urlERGO)
dataOut = data.json()

print(dataOut)