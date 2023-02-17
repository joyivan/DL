import os

import numpy as np
from PIL import Image

def readImgAndAddToVol(totalArray,filename,i):
    image=Image.open(filename)
    image=image.convert('L')
    image_array=np.array(image)
    totalArray[:,:,i-301]=image_array
    return totalArray

def VolToHatViewJpg(VolFileName):
    print('input file shape is',VolFileName.shape)
    for i in range(VolFileName.shape[0]):
        image=VolFileName[i,:,:]
        #image = image.convert('RGB')
        #print(image.shape)
        #AssertionError('pause')
        #image=image.transpose(1,0)
        image=Image.fromarray(image)
        image=image.convert('L')
        image.save('hatView'+str(i)+'.jpg')
    print('ok')
import os
if __name__=='__main__':
    fileDir='/Users/joyivan/Downloads/temp11/se4'
    os.chdir(fileDir)
    fileList=os.listdir()
    '''
    for i in range(len(fileList)):
        os.rename(fileList[i],fileList[i][-11:-4])
    '''

    VolTotal=np.zeros((512,512,310))
    count=len(fileList)
    for i in range(301,611):
       VolTotal=readImgAndAddToVol(VolTotal,str(i)+'.jpg',i)

    #print(VolTotal[:,:,309])
    #im=VolTotal[60,:,:]

    #im=Image.fromarray(im)
    #im.show()
    VolToHatViewJpg(VolTotal)
