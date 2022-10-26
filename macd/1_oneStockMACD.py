"""

"""
import pandas_datareader as pd
import datetime

# pd.set_option('expand_frame_repr', False)  # Lines no wrapping
# pd.set_option('display.max_rows', 50000)  # Maxi rows

#
# df = pd.read_csv('tsla_d_sep.csv', encoding='gbk', skiprows=1, parse_dates=['Date'])
start = datetime.datetime(2022,1,1)
end = datetime.datetime(2022,10,20)
df = pd.DataReader('TSLA','stooq',start,end)
df.sort_index(inplace=True,ascending=True)
print(df)
# Weighting factor
# pre_close
shifted = df['Close'].shift()
#print(shifted)
df['pre_Close'] = shifted
df['wf'] = (df['Close'] / df['pre_Close']).cumprod()
df['close_wf'] = df['wf'] * (df.iloc[-1]['Close'] / df.iloc[-1]['wf'])
print(df)

# 计算MACD
df['EMA_short'] = df['close_wf'].ewm(span=12, adjust=False).mean()
df['EMA_long'] = df['close_wf'].ewm(span=26, adjust=False).mean()
df['DIF'] = df['EMA_short'] - df['EMA_long']
df['DEA'] = df['DIF'].ewm(span=9, adjust=False).mean()
df['MACD'] = (df['DIF'] - df['DEA']) * 2

print(df)
