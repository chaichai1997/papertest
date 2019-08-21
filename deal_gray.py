# -*- coding: utf-8 -*-
# author = "chaichai"
import pandas as pd
from numpy import *
import seaborn as sns

f = open('F:\\zhang\\papertest\\result.csv')
data = pd.read_csv(f, header=None)  # len(data) 3114 len(columns) 18
s = [
    [0, 1, 2, 3],
    [1, 0, 2, 3],
    [2, 3, 0, 1],
    [3, 2, 0, 1],
    [4, 5, 6, 7],
    [5, 4, 6, 7],
    [6, 7, 8, 9],
    [7, 6, 8, 9],
    [8, 9, 10, 11],
    [9, 8, 10, 11],
    [10, 11, 12, 13],
    [11, 10, 12, 13],
    [12, 13, 10, 11],
    [13, 12, 10, 11],
    [14, 15, 16, 17],
    [15, 14, 16, 17],
    [16, 17, 15, 14],
    [17, 16, 15, 14]
]
ds = 0
df = 18
a1 = []
a2 = []
while df < len(data):
    DF = data.iloc[ds:df, ]
    DF.index = [i for i in range(18)]
    b = []
    r = []
    for i in range(len(DF)):
        d = (DF.iloc[i, s[i][1]]+DF.iloc[i, s[i][2]]+DF.iloc[i, s[i][3]])/3
        b.append(d)
        if d > 0.8:
            r.append('0')
        elif 0.6 < d <= 0.8:
            r.append('1')
        else:
            r.append('2')
    a1.append(b)
    a2.append(r)
    ds += 18
    df += 18
result1 = pd.DataFrame(a1)
result1.to_csv("deal_gray_result.csv", index=False, header=False, mode='a')
result2 = pd.DataFrame(a2)
result2.to_csv("label.csv", index=False, header=False, mode='a')





