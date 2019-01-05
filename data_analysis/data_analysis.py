import pandas as pd
import numpy as np
from classes.DataFrame import DataFrame
import matplotlib.pyplot as plt
import statsmodels.api as sm
import time

plt.style.use('fivethirtyeight')

tic = time.time()

df = DataFrame('../data/data.txt').df

toc = time.time()
print("Time taken to create the Dataframe: ", (toc - tic), " seconds")

#print(df.info())

tic = time.time()

plt.figure(figsize=(20, 10))

plt.subplot(4, 1, 1)
mean = pd.Series(df['Energy Mean']).asfreq('S')
mean.plot()

plt.subplot(4, 1, 2)
stddev = pd.Series(df['Energy Std. Deviation']).asfreq('S')
stddev.plot()

plt.subplot(4, 1, 3)
pp = mean.resample('H').mean()
pp.plot()

plt.subplot(4, 1, 4)
ts = stddev.resample('H')
ts.plot()

toc = time.time()
print("Time taken to plot the Dataframe: ", (toc - tic), " seconds")


#ts = stddev
#decomposed = sm.tsa.seasonal_decompose(ts, freq=12) # The frequncy is annual
#figure = decomposed.plot()
plt.show()


