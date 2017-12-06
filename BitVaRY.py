import cryptoextract
import numpy as np
import pandas as pd
from joblib import Parallel, delayed
import operator
import matplotlib.pyplot as plt
import ClusterLib
from ClusterLib.clusterlib import *
from ClusterLib.distlib import *

p=cryptoextract.Price()
#coinlist={"BTC":{"Id":"1182","Url":"/coins/btc/overview","ImageUrl":"/media/19633/btc.png","Name":"BTC","Symbol":"BTC","CoinName":"Bitcoin","FullName":"Bitcoin (BTC)","Algorithm":"SHA256","ProofType":"PoW","FullyPremined":"0","TotalCoinSupply":"21000000","PreMinedValue":"N/A","TotalCoinsFreeFloat":"N/A","SortOrder":"1","Sponsored":false}}
coinList = p.coinList()
coins = sorted(list( coinList['Data'].keys() ))
h = cryptoextract.History()

df_dict = {}
for coin in coins:
    histo = h.histoDay(coin, 'USD', allData=True)
    if histo['Data']:
        df_histo = pd.DataFrame(histo['Data'])
        df_histo['time'] = pd.to_datetime(df_histo['time'], unit='s')
        df_histo.index = df_histo['time']
        del df_histo['time']
        del df_histo['volumefrom']
        del df_histo['volumeto']

        df_dict[coin] = df_histo
crypto_histo = pd.concat(df_dict.values(), axis=1, keys=df_dict.keys())
histo_coins = [elem for elem in crypto_histo.columns.levels[0] if not elem == 'MYC']
histo_length = {}
for coin in histo_coins:
    histo_length[coin] = np.sum(~np.isnan(crypto_histo[coin]['close'].values))

sorted_length = sorted(histo_length.items(), key=operator.itemgetter(1), reverse=True)
histo_length = {}
for coin in histo_coins:
    histo_length[coin] = np.sum(~np.isnan(crypto_histo[coin]['close'].values))

sorted_length = sorted(histo_length.items(), key=operator.itemgetter(1), reverse=True)
sub_coins = [sorted_length[i][0] for i in range(300)]

sub_crypto_histo = crypto_histo[sub_coins]
sub_crypto_histo.tail()