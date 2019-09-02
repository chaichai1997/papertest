import pandas as pd
from numpy import *
import seaborn as sns 
import matplotlib.pyplot as plt

f = open('F:\\zhang\\papertest\\data.csv')
data = pd.read_csv(f, header=None)  # len(data) 4153 len(columns) 22
data = data.sample(frac=1.0)


def GRA_ONE(DataFrame, m=0):
    gray = DataFrame   # 读取为df格式
    gray = (gray - gray.min()) / (gray.max() - gray.min())   # 标准化
    std = gray.iloc[:, m]  # 第m列为标准要素
    ce = gray.iloc[:, 0:]  # 其余列为比较要素
    n = ce.shape[0]  # 行数
    m = ce.shape[1]  # 列数
    # 与标准要素比较，相减
    a = zeros([m, n])
    for i in range(m):
        for j in range(n):
            a[i, j] = abs(ce.iloc[j, i]-std[j])

    # 取出矩阵中最大值与最小值
    c = amax(a)
    d = amin(a)   # 计算值
    result = zeros([m, n])

    for i in range(m):
        for j in range(n):
            result[i, j] = (d+0.5*c)/(a[i, j]+0.5*c)   # 分辨系数0.5

    # 求均值，得到灰色关联值
    result2 = zeros(m)
    for i in range(m):
        result2[i] = mean(result[i, :])
    RT = pd.DataFrame(result2)
    return RT


def GRA(DataFrame):
    ds = 0
    df = 24
    while df < len(DataFrame):
        data = DataFrame.iloc[ds:df, ]
        data.index = [i for i in range(24)]
        list_columns = [str(s) for s in range(len(data.columns)) if s not in [None]]
        df_local = pd.DataFrame(columns=list_columns)
        for i in range(len(data.columns)):
            df_local.iloc[:, i] = GRA_ONE(data, m=i)[0]
        df_local.to_csv("result.csv", index=False, header=False, mode='a')
        ds += 24
        df += 24
        # ShowGRAHeatMap(df_local)
    return df_local


# 灰色关联结果矩阵可视化
def ShowGRAHeatMap(DataFrame):
    colormap = plt.cm.RdBu
    plt.figure(figsize=(16, 8))
    plt.title('Gray Correlation of Features', y=1, size=15)
    sns.heatmap(DataFrame.astype(float), linewidths=0.1, vmax=1.0, square=True, cmap=colormap,
                linecolor='white', annot=True)
    plt.show()


if __name__ == '__main__':
    data_gra = GRA(data)
    # ShowGRAHeatMap(data_gra)
