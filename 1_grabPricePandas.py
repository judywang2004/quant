import pandas as pd
import matplotlib.pyplot as plt

#local local tsla_d_sep.csv file as DataFramee
df = pd.read_csv('tsla_d_sep.csv')

#inspect the data
print(df)
#show some summary statistics
print(df.describe())

# reindex data using a datatimeindex
df.set_index(pd.DatetimeIndex(df['Date']), inplace=True)

#keep only the column 'Close' Value
#df = df[['Close']]

#re-inspect data
print(df)

#print info
#print(df.info())

#Scatter plot with date against price
plt.scatter(df['Date'],df['Close'])
plt.title("Scatter Plot")

plt.xlabel('Date')
plt.ylabel('Price')
plt.colorbar()
plt.show()


