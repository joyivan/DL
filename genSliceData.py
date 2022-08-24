import shutil
import os
import numpy as np




def creatDir(Dir):
    if not os.path.isdir(Dir):
        os.makedirs(Dir)
def cpDir(source,destinst):
            print(source+'/'+i)
            print(destinst+'/')
            shutil.copyfile(source+'/'+i,destinst+'/'+i)

work_dir='/media/joyivan/OLD/data/CT_MD_JPG/'

if __name__=='__main__':
    sliceInfo=np.load(work_dir+'Slice-level-labels.npy')
    print('sliceInfo data type is '+str(type(sliceInfo)))
#0-54:covid  55:79:cap
    destDir=work_dir+'sliceData'+'/covidSlice'
    creatDir(destDir)
    for i in range(1,55):
        sliceIndex=np.where(sliceInfo[i]==1)
        for j in sliceIndex[0]:
            shutil.copyfile(work_dir+'sliceData/covid-19/P'+str(i).zfill(3)+'/IM'+str(j).zfill(4)+'.jpg',destDir+'/P'+\
                            str(i).zfill(3)+'_'+'IM'+str(j).zfill(4)+'.jpg')
