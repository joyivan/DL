#today is good day which comes from mbp
#e212121212   big machine from 
#test git push cach user and pwd
#test mbp from  20220728
import numpy as np
from PIL import Image
import pandas as pd
import os
import matplotlib.pyplot as plt
import torch
import time
def decor(func):
    def wrapper(*arg):
        t1=time.time()
        result=func(*arg)
        t2=time.time()
        print('waste time is {}'.format(t2-t1))
        return result
    return wrapper
#add=decor(add)
@decor
def add(x,y):
    return x+y
def panduan(sex):
    def func1(func):
         def func2():
             if sex=='boy':
                 print('buy car!')
             elif sex=='girl':
                 print('buy cloth!')
             return func()
         return func2
    return func1
@panduan(sex='boy')
def man():
    print("好好上班man")
@panduan(sex='girl')
def woman():
    print("好好上班woman")

if __name__=='__main__':
    '''
    for i in range(3):
        print(i)
    print(add(1,3))
    print(torch.cuda.is_available())
'''
man()
#def readData()
woman()
xs=[]
'''
for year in np.arange(1999,2016,1):

      for month in np.arange(1,13,1):
           print year,month
           if month<10 :
              xs.append(pd.read_csv('DATA'+str(year)+'0'+str(month)+'_NSW1.csv'))
           else :
              xs.append(pd.read_csv('DATA'+str(year)+str(month)+'_NSW1.csv'))


for i in np.arange(0,len(xs),1):
      yy=xs[i]
      yyy=np.array(yy['TOTALDEMAND'])
      if i==0:
         yyyy=yyy
      else :
         yyyy=np.concatenate((yyyy,yyy))

'''
