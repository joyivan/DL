#前提条件是利用ImageJ将文件保存为BMP  512*512灰度图


#当前程序需要到数据所在文件夹以sudo python 互动命令行运行 因为该文件夹下全是bmp灰#度图
#导入需求包

import numpy as np 
import Image
import pandas as pd
import os
import matplotlib.pyplot as plt

#读入文件
filelist=np.array(os.listdir(os.getcwd()))  
ls=np.zeros(shape=(filelist.size,512*512))
x=0
for i in filelist:
  
  #f[x]=Image.open(i)
  #将文件读入一维数组
  ls[x]=np.array(Image.open(i).getdata())
  x=x+1

row,col=ls.shape
#转换为pandas对象
df=pd.DataFrame(ls,dtype=int)
#将262444列 也就是最后一列后面加入类别标号 red:1 blue:0
df.loc[:,-1]=0

#保存到 /home 下csv文件
df.to_csv('/home/blue.csv')
#更改到red_resize工作路径
os.chdir('/home/joyivan/downloads/\xe6\x96\xb0\xe5\xbb\xba\xe6\x96\x87\xe4\xbb\xb6\xe5\xa4\xb9\xe7\xad\x892\xe4\xb8\xaa\xe6\x96\x87\xe4\xbb\xb6/red_resize')


#读取目录下的csv文件到x
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
train_x=train_x.astype(np.float32)
#将读出来的X一维数组变成512×512
#d=a.reshape((2,4))

#save current data to filesystem
import cPickle as ck
myfile1=file('train.data','a')
ck.dump(train,myfile1)
myfile2=file('test.data','a')
ck.dump(test,myfile2)
myfile3=file('z.data','a')
ck.dump(z,myfile3)
#load data from file  eg:
 myFile =file('z.data','r')
 myList=p.load(myFile)

#更改大小目的时显示样本
ll=ls[2,:].reshape((512,512))
#灰度参数
cmap = plt.cm.gray

plt.imshow(ll,cmap=cmap)
plt.show()


