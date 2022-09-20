from profitability import Profitability

ergo = Profitability('ERG','USD', 130, 220)
raven = Profitability('RVN','USD', 22, 220)

print(ergo.get_price())
print(raven.get_network_hashrate())
