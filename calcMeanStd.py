import os.path
import matplotlib.pyplot as plt
import random
import numpy as np
import torch.cuda

from readPickleFile import readFile as rp
from PIL import Image
dataDir="/home/joyivan/PycharmProjects/pythonProject1/data/cifar-10-batches-py"
if __name__=="__main__":
    temp=rp(os.path.join(dataDir,"trainData"))
    fileName,label=temp[0],temp[1]
    print(len(fileName))
    dataScale=1000
    img_w,img_h=32,32
    imgs=np.zeros([img_w,img_h,3,1])
    means,stdevs=[],[]
    random.seed(666)
    random.shuffle(fileName)
    for i in range(dataScale):
        img=Image.open(os.path.join(dataDir,'train',fileName[i]))

        img=img.resize((img_w,img_h))
        img=np.array(img)

        imgs=np.concatenate((imgs,img[:,:,:,np.newaxis]),axis=3)
    '''
    print(imgs[:,:,:,dataScale].shape)
    plt.imshow(imgs[:,:,:,dataScale]/255)
    plt.show()
    '''
    imgs=imgs/255
    for i in range(3):
        oneDimension=imgs[:,:,i,:].ravel()
        means.append(np.mean(oneDimension))
        stdevs.append(np.std(oneDimension))

        #means.reverse() # BGR --> RGB


    print(means)
    print(stdevs)
