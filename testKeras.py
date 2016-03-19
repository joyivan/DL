import numpy as np 
import Image
import pandas as pd
import os
import matplotlib.pyplot as plt

from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Convolution2D, MaxPooling2D
from keras.optimizers import SGD

x=pd.read_csv('red128.csv')
x=np.array(x)
#删除第一列标号
x=x[:,1:]

y=pd.read_csv('blue128.csv')
y=np.array(y)
y=y[:,1:]
z=np.vstack((x,y))

#随机取样形成train 和 test 并分开train_x 与train_y  test_x test_y
np.random.shuffle(z)
train,test=z[:200,:],z[201:,:]
X_train=train[:,:16384]
y_train=train[:,16384]


model = Sequential()
# input: 100x100 images with 3 channels -> (1, 100, 100) tensors.
# this applies 32 convolution filters of size 3x3 each.
model.add(Convolution2D(32, 3, 3, border_mode='valid', input_shape=(1,128, 128)))
model.add(Activation('relu'))
model.add(Convolution2D(32, 3, 3))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Convolution2D(64, 3, 3, border_mode='valid'))
model.add(Activation('relu'))
model.add(Convolution2D(64, 3, 3))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Flatten())
# Note: Keras does automatic shape inference.
model.add(Dense(256))
model.add(Activation('relu'))
model.add(Dropout(0.5))

model.add(Dense(10))
model.add(Activation('softmax'))

sgd = SGD(lr=0.1, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd)
#  XX_train=X_train.reshape(-1,1,128,128) 1-D  to 2D

model.fit(XX_train, y_train, batch_size=32, nb_epoch=1)

