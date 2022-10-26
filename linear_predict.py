import pandas_datareader.data as web
import datetime

start = datetime.datetime(2022,1,1)
end = datetime.datetime(2022,10,20)
df = web.DataReader('TSLA','stooq',start,end)
df.sort_index(inplace=True,ascending=True)
print(df)

predict_count = 30
df['label'] = df['Close'].shift(-predict_count)
print(df)

x = df.drop(['label'],axis=1)
y = df['label'][:-predict_count]
print(y)

from sklearn.preprocessing import StandardScaler
scale = StandardScaler()
scale.fit(x)
x = scale.transform(x)
print(x)
x_lately = x[-predict_count:]
x = x[:-predict_count]
print(len(x))
print(len(x_lately))

#
from sklearn.model_selection import train_test_split
x_train,y_train,x_test,y_test = train_test_split(x,y,test_size=0.2)
print(len(x_train))
print(len(y_train))






