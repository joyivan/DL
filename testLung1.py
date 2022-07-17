#lalalal
import numpy as np 
#test row 
import Image
import pandas as pd
import os
import matplotlib.pyplot as plt
x=pd.read_csv('red.csv')
x=np.array(x)
#删除第一列标号
x=x[:,1:]

y=pd.read_csv('blue.csv')
y=np.array(y)
y=y[:,1:]
z=np.vstack((x,y))

#随机取样形成train 和 test 并分开train_x 与train_y  test_x test_y
np.random.shuffle(z)
train,test=z[:200,:],z[201:,:]
train_x=train[:,:262144]
train_y=train[:,262144]
X=train_x.astype(np.int8)
y=train_y.astype(np.int8)
from lasagne import layers
from lasagne.updates import nesterov_momentum
from nolearn.lasagne import NeuralNet

net1 = NeuralNet(
    layers=[  # three layers: one hidden layer
        ('input', layers.InputLayer),
        ('hidden', layers.DenseLayer),
        ('output', layers.DenseLayer),
        ],
    # layer parameters:
    input_shape=(None, 262144),  # 96x96 input pixels per batch
    hidden_num_units=130,  # number of units in hidden layer
    output_nonlinearity=None,  # output layer uses identity function
    output_num_units=1,  # 30 target values

    # optimization method:
    update=nesterov_momentum,
    update_learning_rate=0.01,
    update_momentum=0.9,

    regression=True,  # flag to indicate we're dealing with regression problem
    max_epochs=400,  # we want to train this many epochs
    verbose=1,
    )
net1.fit(X, y)
