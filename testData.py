import numpy as np
import matplotlib.pyplot as plt
import pickle
import re
import os
filelist =os.listdir("/home/joyivan/PycharmProjects/pythonProject1/data/cifar-10-batches-py")
os.chdir("/home/joyivan/PycharmProjects/pythonProject1/data/cifar-10-batches-py")
pattern="data_"
def unpickle(file):
    with open(file,'rb') as fo:
        dict_=pickle.load(fo,encoding="bytes")
    return dict_
temp_file=[]
for i in filelist:
    if re.match(pattern,i):
        print('ok')

        temp_file.append(unpickle(i))
    else:
        print('fail')

print(filelist)
imageData=temp_file[0][b'data']
image=imageData[0].reshape((3,32,32))
image=image.transpose((1,2,0))
print(image.shape)
plt.imshow(image)
plt.show()
print(imageData[0].shape)