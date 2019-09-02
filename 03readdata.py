# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

"""
将label.CSV文件写入y.CSV 二维变一维度
"""
# f2 = open('label.csv')
# f3 = open('x.csv')
# y = pd.read_csv(f2, header=None, dtype=object)
# x = pd.read_csv(f3, header=None)
# a = []
# b = []
# for i in range(169):   # 共169条数据
#     y_i = y.iloc[i]    # 获取每一行
#     for j in y_i:   # 读取每行中元素，生成列表
#         print(j)
#         if j == '0':
#             a = [1, 0, 0]
#         elif j == '1':
#             a = [0, 1, 0]
#         elif j == '2':
#             a = [0, 0, 1]
#         b.append(a)
# data = pd.DataFrame(b)
# data.to_csv("y.csv", index=False, header=False, mode='a')  # 写入文件

"""
将x写入x.CSV文件
"""
# f1 = open('F:\\zhang\\papertest\\data.csv')
# x = pd.read_csv(f1, header=None)
# ds = 0
# df = 24
# for i in range(169):
#     x_i = x.iloc[ds:df]
#     for j in range(18):
#         s = x_i.iloc[:, j]
#         a = []
#         a.append(s)
#         d = pd.DataFrame(a)
#         d.to_csv("x.csv", index=False, header=False, mode='a')
#     ds += 24
#     df += 24


"""
x+y
"""
# f3 = open('x.csv')
# x = pd.read_csv(f3, header=None)
# f4 = open('y.csv')
# y = pd.read_csv(f4, header=None)
# result = pd.concat([x, y], axis=1)
# result.to_csv('x+y.csv', index=False, header=False)

"""
打乱数据
"""
f5 = open('x+y.csv')
data = pd.read_csv(f5, header=None)
data = data.sample(frac=1.0)
data = data.reset_index()
x = data.iloc[:, 1:25]
y = data.iloc[:, 25:]
x.to_csv('x_s.csv', index=False, header=False)
y.to_csv('y_s.csv', index=False, header=False)
