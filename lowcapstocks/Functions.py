import pandas as pd

pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 5000)  # 最多显示数据的行数


# 计算策略评价指标
def strategy_evaluate(select_stock):
    """
    :param select_stock: 每周期选出的股票
    :return:
    """
    results = pd.DataFrame()
    # ===计算累积净值
    results.loc[0, '累积净值'] = round(select_stock['累积净值'].iloc[-1], 2)
    # ===计算年化收益
    annual_return = (select_stock['累积净值'].iloc[-1]) ** (
            '1 days 00:00:00' / (select_stock['交易日期'].iloc[-1] - select_stock['交易日期'].iloc[0]) * 365) - 1
    results.loc[0, '年化收益'] = str(round(annual_return * 100, 2)) + '%'

    # # 计算当日之前的资金曲线的最高点
    select_stock['max2here'] = select_stock['累积净值'].expanding().max()
    # # 计算到历史最高值到当日的跌幅，drowdwon
    select_stock['dd2here'] = select_stock['累积净值'] / select_stock['max2here'] - 1
    # # 计算最大回撤，以及最大回撤结束时间
    end_date, max_draw_down = tuple(select_stock.sort_values(by=['dd2here']).iloc[0][['交易日期', 'dd2here']])
    # # 计算最大回撤开始时间
    start_date = select_stock[select_stock['交易日期'] <= end_date].sort_values(by='累积净值', ascending=False).iloc[0]['交易日期']
    # 将无关的变量删除
    select_stock.drop(['max2here', 'dd2here'], axis=1, inplace=True)
    results.loc[0, '最大回撤周期'] = format(max_draw_down, '.2%')
    results.loc[0, '最大回撤周期开始时间'] = str(start_date)
    results.loc[0, '最大回撤周期结束时间'] = str(end_date)
    results.loc[0, '年化收益/回撤比'] = round(annual_return / abs(max_draw_down), 2)
    return results.T

