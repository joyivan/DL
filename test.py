import pydicom
import numpy as np
work_dir='/media/joyivan/OLD/data/CT_MD_JPG'
orginDIR='Cap_Cases'
data0=pydicom.read_file(work_dir+'/'+orginDIR+'/cap003/'+'checkedIM0134.dcm')
data1=pydicom.dcmread(work_dir+'/'+orginDIR+'/cap003/'+'checkedIM0134.dcm')
print(data0)
print(data0[0x0020,0x1041].value)
pixArray=np.array(data0.pixel_array)
print(np.max(pixArray))
from playsound import playsound
playsound("/home/joyivan/Downloads/non.mp3")


import math
def normal_distribution(x): #处理x<0(目标点在分布中心左侧)的情况
    if x<0:
        return 1-normal_distribution(-x)
    if x==0:
        return 0.5 #求标准正态分布的概率密度的积分
    s=1/10000
    xk=[]
    for i in range(int(x/s)):
        integral = fx_normal_distribution((i+1)*s )
        xk.append(integral)
        print(integral)
    print(xk[0])
    sum=0
    for each in xk:
        sum+=each
    print(sum)
    return 0.5+sum*s

def fx_normal_distribution(x):
    return math.exp((-(x)**2)/2)/(math.sqrt(2*math.pi))

print(normal_distribution(-6.6))
from scipy.stats import norm

q = norm.cdf(-6.6)  # 累计密度函数
norm.ppf(q)  # 累计密度函数的反函数
print(q)
print(norm.ppf(q)) #可以用来找置信区间
