# -*- coding: utf-8 -*-
# author = "chaichai"
import numpy as np
from keras import models
from keras import layers
import matplotlib.pyplot as plt
import pandas as pd


"""
数据处理
"""
f1 = open('F:\\zhang\\papertest\\x.csv')
x = pd.read_csv(f1, header=None)
f2 = open('F:\\zhang\\papertest\\y.csv')
y = pd.read_csv(f2, header=None)
train_data = np.array(x.iloc[:2000])
train_label = np.array(y.iloc[:2000])
train_label = np.asarray(train_label).astype('float32')
validation_data = np.array(x.iloc[2000:2500])
validation_label = np.array(y.iloc[2000:2500])
validation_label = np.asarray(validation_label).astype('float32')
test_data = np.array(x.iloc[2500:])
test_label = np.array(x.iloc[2500:])
test_data = np.asarray(test_data).astype('float32')

"""
数据标准化
"""
mean = train_data.mean(axis=0)
train_data -= mean
std = train_data.std(axis=0)
train_data /= std
test_data -= mean
test_data /= std
validation_data -= mean
validation_data /= std


"""
构建网络
"""
model = models.Sequential()
model.add(layers.Dense(24, activation='relu', input_shape=(train_data.shape[1],)))
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
    train_data,
    train_label,
    epochs=100,
    batch_size=32,
    validation_data=(validation_data, validation_label)
)
"""
    绘制训练损失与验证损失
"""
loss_value = history.history['loss']
val_loss_value = history.history['val_loss']
epoch = range(1, len(loss_value) + 1)
plt.plot(epoch, loss_value, 'bo', label='Training loss')  # bo,蓝色远点
plt.plot(epoch, val_loss_value, 'b', label='Validation loss')  # 蓝色实线
plt.title('Training and validation loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()
plt.show()
