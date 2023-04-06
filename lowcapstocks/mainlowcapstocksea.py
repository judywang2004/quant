from Evaluate import *
from Functions import *
import warnings
import os

warnings.filterwarnings('ignore')
pd.set_option('expand_frame_repr', False)  # 当列太多时不换行
pd.set_option('display.max_rows', 5000)  # 最多显示数据的行数

_ = os.path.abspath(os.path.dirname(__file__))  # 返回当前文件路径
root_path = os.path.abspath(os.path.join(_, '.'))  # 返回根目录文件夹

# =====导入数据
# 从pickle文件中读取整理好的所有股票数据
df = pd.read_pickle('all_stock_data_M.pkl')

# =====选股
# ===过滤股票
# 剔除不能交易的异常情况
df = df[df['下日_是否交易'] == 1]
df = df[df['下日_开盘涨停'] == False]
# 剔除上市不足1年的新股
df = df[df['上市至今交易天数'] > 250]
# 剔除ST股/退市股
df = df[df['下日_是否ST'] == False]
df = df[df['下日_是否退市'] == False]
# 删除北交所股票
df = df[df['股票名称'].str.contains('bj') == False]
# 确认选股周期，可调
df = df[df['交易日期'] >= pd.to_datetime('2010-01-01')]

"""===按照策略选股：不同策略修改此处即可"""
# 低价股选股：价格最低的50只，且收盘价>=2
df['价格排名'] = df.groupby('交易日期')['收盘价'].rank(ascending=True, pct=False, method='first')
df = df[(df['价格排名'] <= 50) & (df['收盘价'] >= 2)]

# 低价股选股：价格最低的前20%只股票，且收盘价>=2
# df['价格排名'] = df.groupby('交易日期')['收盘价'].rank(ascending=True, pct=True, method='first')
# df = df[(df['价格排名'] <= 0.2) & (df['收盘价'] >= 2)]

# 低价股 + 小市值选股：价格和市值同时满足：最小的前200只股票，且收盘价>=2
# df['价格排名'] = df.groupby('交易日期')['收盘价'].rank(ascending=True, pct=False, method='first')
# df['市值排名'] = df.groupby('交易日期')['总市值'].rank(ascending=True, pct=False, method='first')
# df = df[(df['价格排名'] <= 200) & (df['市值排名'] <= 200) & (df['收盘价'] >= 2)]

# 删除数据
df.dropna(subset=['下周期净值'], inplace=True)

# =====整理选中股票数据
df['股票代码'] += ' '
df['股票名称'] += ' '
group = df.groupby('交易日期')
select_stock = pd.DataFrame()
select_stock['股票数量'] = group['股票名称'].size()
select_stock['买入股票代码'] = group['股票代码'].sum()
select_stock['买入股票名称'] = group['股票名称'].sum()
select_stock['下周期净值'] = group['下周期净值'].mean()
print(select_stock.tail(5))
select_stock.to_csv('低价股策略选股详情.csv', encoding='gbk')
# 计算整体资金曲线
select_stock.reset_index(inplace=True)
select_stock['累积净值'] = select_stock['下周期净值'].cumprod()
results = strategy_evaluate(select_stock)
print(results)
draw_equity_curve_mat(select_stock)
