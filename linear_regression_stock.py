import pandas_datareader.data as pd
import datetime

start = datetime.datetime(2022,1,1)
end = datetime.datetime(2022,10,20)
df = pd.DataReader('TSLA','stooq',start,end)
df.sort_index(inplace=True,ascending=False)
print(df)

import numpy as np
X = df.iloc[:,0].to_numpy().reshape(-1,1)
Y = df.iloc[:,1].to_numpy().reshape(-1,1)

from sklearn.linear_model import LinearRegression
linear_regressor = LinearRegression()
linear_regressor.fit(X,Y)
Y_pred = linear_regressor.predict(X)

import matplotlib.pyplot as plt
plt.scatter(X,Y)
plt.plot(X,Y_pred,color='red')
plt.show()


