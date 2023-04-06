import matplotlib.pyplot as plt


# 绘制策略曲线
def draw_equity_curve_mat(df):
    """
    绘制策略曲线
    :param df: 包含净值数据的df
    :return:
    """
    # 复制数据
    draw_df = df.copy()
    plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'SimHei']
    plt.rcParams['axes.unicode_minus'] = False

    plt.figure()
    # 绘制左轴数据
    plt.plot(draw_df['交易日期'], draw_df['累积净值'], linewidth=2, label='累积净值')
    # 设置坐标轴信息等
    plt.ylabel('净值')
    plt.show()

