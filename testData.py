import numpy as np
import matplotlib.pyplot as plt
import pickle
import re
import os
import cv2

'''
1.include put original data that download fr cifar10 into train and test directory and each file locate\
in different directory which name is the classLabel
2.include creatDir tool that can create directory
3.include unpickle tool that can get pickle file which is belongs the to filesystem.


'''
def creatDir(Dir):
    if not os.path.isdir(Dir):
        os.mkdir(Dir)
def unpickle(file):
    with open(file,'rb') as fo:
        dict_=pickle.load(fo,encoding="bytes")
    return dict_
def getIMGfromOrgFile():
    temp_file=[]
    workDir = "/home/joyivan/PycharmProjects/pythonProject1/data/cifar-10-batches-py"
    dataDir = os.path.join(workDir)
    print(dataDir)
    filelist = os.listdir(workDir)
    os.chdir(workDir)
    pattern = "data_"

    def creatDir(Dir):

        for i in filelist:
        if re.match(pattern,i):
            print('ok')
            temp_file.append(unpickle(i))
        else:
            print('fail')
    metaDict=unpickle('batches.meta')
    print(metaDict.keys())
    metaLabel_names=metaDict[b'label_names']
    for i in temp_file:
        for j in range(len(i[b'filenames'])):
           image=i[b'data'][j].reshape((3,32,32))
           image=image.transpose((1,2,0))
           imageLabel=i[b'labels'][j]
           imageFileName=i[b'filenames'][j]
           creatDir(os.path.join(dataDir,"train",str(imageLabel)))
           cv2.imwrite(os.path.join(dataDir,"train",str(imageLabel),str(imageFileName,'utf-8')),image)

    print("train data processing task finished!")

    test_batch_file=unpickle('test_batch')
    for j in range(len(test_batch_file[b'filenames'])):
        image = test_batch_file[b'data'][j].reshape((3, 32, 32))
        image = image.transpose((1, 2, 0))
        imageLabel = test_batch_file[b'labels'][j]
        imageFileName = test_batch_file[b'filenames'][j]
        creatDir(os.path.join(dataDir, "test", str(imageLabel)))
        cv2.imwrite(os.path.join(dataDir, "test", str(imageLabel), str(imageFileName, 'utf-8')), image)
    print("test data processing task finished!")
from getMyData import getData
def testGetMyData():
   data=getData(flag='train')
   file,label=data.__getitem__(1)
   print(file)
   print(label)
if __name__ == "__main__":
    testGetMyData()
