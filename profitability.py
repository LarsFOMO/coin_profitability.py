#   INFO
#https://pypi.org/project/cryptocompare/ 

from dataclasses import replace
import json
import datetime
from unicodedata import name
import pandas as pd
import matplotlib.pyplot as plt
import requests
import cryptocompare
import re
from os.path import join

urlERGO = "https://min-api.cryptocompare.com/data/blockchain/mining/calculator?fsyms=ERG&tsyms=USD"
urlRAVEN = "https://min-api.cryptocompare.com/data/blockchain/mining/calculator?fsyms=RVN&tsyms=USD"

class Profitability:

    def __init__(self, name, currency1, hashrate, powerUse):
        self.name = name
        self.currency1 = currency1
        self.hashrate = hashrate
        self.powerUse = powerUse
    
    def get_price(self):
        self.price = cryptocompare.get_historical_price(self.name,self.currency1)      #130MH/s
        string1 = str(self.price)
        num1 = re.findall(r"[-+]?(?:\d*\.\d+|\d+)", string1)
        self.price = ''.join(map(str,num1))
        return self.price

    def get_network_hashrate(self):
        url1 = "https://min-api.cryptocompare.com/data/blockchain/mining/calculator?fsyms="
        url2 = "&tsyms="
        fullURL = url1 + self.name + url2 + self.currency1
        data = requests.get(fullURL)
        dataOut = data.json()
        oo = [int(x) for x in re.findall(r' \d+', str(dataOut))]
        network_hashrate = oo[1]
        return network_hashrate

