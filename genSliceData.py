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
    sliceInfo=np.load(work_dir+'Slice-level-labels-updated-1.npy',allow_pickle=True)
    print('sliceInfo data type is '+str(type(sliceInfo)))
#1-54:covid  55:79:cap
    destDir=work_dir+'sliceData'+'/covidSlice'
    creatDir(destDir)
    for i in range(1,55):
        sliceIndex=np.where(sliceInfo[i-1]==1)
        for j in sliceIndex[0]:
            shutil.copyfile(work_dir+'sliceData/covid-19/P'+str(i).zfill(3)+'/IM'+str(j).zfill(4)+'.jpg',destDir+'/P'+\
                            str(i).zfill(3)+'_'+'IM'+str(j).zfill(4)+'.jpg')
    print('covid finish!0')
    destDir = work_dir + 'sliceData' + '/capSlice'
    creatDir(destDir)
    for i in range(1,25):
        sliceIndex = np.where(sliceInfo[i+54 ] == 1)
        for j in sliceIndex[0]:
            shutil.copyfile(work_dir+'sliceData/cap/cap'+str(i).zfill(3)+'/IM'+str(j).zfill(4)+'.jpg',destDir+'/cap'+ \
                            str(i).zfill(3) + '_' + 'IM' + str(j).zfill(4) + '.jpg')
    print('cap finish')
