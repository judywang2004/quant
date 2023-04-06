import pandas_datareader.data as pd
import datetime

start = datetime.datetime(2022,1,1)
end = datetime.datetime(2022,10,20)
df = pd.DataReader('TSLA','stooq',start,end)
df.sort_index(inplace=True,ascending=False)
print(df)

predict_count = 1
df['label'] = df['Close'].shift(-predict_count)
import numpy as np
predict_count =1
X = df.drop(['label'],axis=1)
Y = df['label'][:-predict_count]

from sklearn.linear_model import LinearRegression
scale = StandardScaler()
scale.fit(X)
X = scale.transform(X)
X_latest = X[-predict_count:]
X=X[:-predict_count]

import matplotlib.pyplot as plt
plt.scatter(X,Y)
plt.plot(X,Y_pred,color='red')
plt.show()


