import numpy as np 
import Image
import pandas as pd
import os
import matplotlib.pyplot as plt


#def readData()
  
  xs=[]
    
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

        
