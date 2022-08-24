import os
import glob
import random
import shutil
import pickle
train_percent=0.9
valid_percent=0.1
workDir="/home/joyivan/PycharmProjects/pythonProject1/data/cifar-10-batches-py"
def creatDir(Dir):
    if not os.path.isdir(Dir):
        os.mkdir(Dir)
def saveFile(DIR,fileName,data):
    with open(os.path.join(DIR,fileName),'wb') as fo:
        pickle.dump(data,fo)
    print('save file finished!')
os.chdir(workDir)
trainLabel=[]
trainFileName=[]
validLabel=[]
validFileName=[]
for root,dirs,files in os.walk(os.path.join(workDir,'train')):
    for dir in dirs:
        imgList=glob.glob(os.path.join(root,dir,'*.png'))
        random.seed(666)
        random.shuffle(imgList)
        train_point=len(imgList)*train_percent
        for indexOfFileList in range(len(imgList)):
            if indexOfFileList<train_point:
                creatDir(os.path.join(workDir,'train'))
                shutil.copy(imgList[indexOfFileList],os.path.join(workDir,'train'))
                fileTemp=os.path.split(imgList[indexOfFileList])
                trainLabel.append(dir)
                trainFileName.append(fileTemp[-1])

            else:
                creatDir(os.path.join(workDir,'valid'))
                shutil.copy(imgList[indexOfFileList], os.path.join(workDir, 'valid'))
                fileTemp=os.path.split(imgList[indexOfFileList])
                validLabel.append(dir)
                validFileName.append(fileTemp[-1])
saveFile(workDir,'trainData',[trainFileName,trainLabel])
saveFile(workDir,'validData',[validFileName,validLabel])
