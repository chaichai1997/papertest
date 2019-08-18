# -*- coding: utf-8 -*-
# author = "chaichai"
import numpy as np
from keras import models
from keras import layers
import matplotlib.pyplot as plt

"""
构建网络
"""
model = models.Sequential()
model.add(layers.Dense(24, activation='relu', input_shape=()))
model.add(layers.Dense(73, activation='relu'))
model.add(layers.Dense(121, activation='relu'))
model.add(layers.Dense(121, activation='relu'))
model.add(layers.Dense(97, activation='relu'))
model.add(layers.Dense(3, activation='softmax'))


"""
模型编译
"""
model.compile(
    optimizer='rmsprop',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)
history = model.fit(

)