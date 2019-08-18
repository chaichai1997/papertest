# -*- coding: utf-8 -*-
import pandas as pd
from numpy import *


f2 = open('F:\\zhang\\papertest\\label.csv')
y = pd.read_csv(f2, header=None)
a = []
for i in range(169):
    y_i = y.iloc[i]
    for j in y_i:
        a.append(j)
data = pd.DataFrame(a)
data.to_csv("y.csv", index=False, header=False, mode='a')

# f1 = open('F:\\zhang\\papertest\\data.csv')
# f2 = open('F:\\zhang\\papertest\\label.csv')
# x = pd.read_csv(f1, header=None)
# y = pd.read_csv(f2, header=None)
# ds = 0
# df = 24
# for i in range(169):
#     x_i = x.iloc[ds:df]
#     x_i.index = [i for i in range(24)]
#     y_i = y.iloc[i]
#     y_i.index = [0]
#     for j in range(18):
#         x_j = x_i.iloc[,:j]