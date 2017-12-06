import pandas as pd
import pandas_datareader as web
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')

start=dt.datetime(2017, 1, 3)
end=dt.datetime(2017,12,5)

prices=web.DataReader('BTC-USD','yahoo', start, end)['Close'] #give option for EUR, INR
returns=prices.pct_change()
last_price=prices[-1]

#Number of simulations
num_simulations=1000
days=336
sim_df=pd.DataFrame()
for x in range(num_simulations):
    count=0
    daily_volatility=returns.std()
    price_series=[]
    price=last_price*(1+np.random.normal(0,daily_volatility))
    price_series.append(price)

    for y in range(days):
        if count==336:
            break
        price=price_series[count]*(1+np.random.normal(0,daily_volatility))
        price_series.append(price)
        count+=1

    sim_df[x]=price_series

fig=plt.figure()
fig.suptitle('Monte Carlo Simulation for predicting the value of BITCOINS')
plt.plot(sim_df)
plt.axhline(y=last_price, color='r',linestyle='-')
plt.xlabel('Day')
plt.ylabel('Price')
plt.show()
