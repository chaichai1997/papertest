# -*- coding: utf-8 -*-
import pandas as pd
from numpy import *

f = open('F:\\zhang\\papertest\\naoduxx.csv')
data = pd.read_csv(f, header=None)
print(len(data.columns))
print(len(data))
dataframe = data.iloc[:, :18]
dataframe.to_csv("data.csv", index=False, header=False)
