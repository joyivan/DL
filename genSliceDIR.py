import os
import shutil
import pandas as pd
import numpy as np
# data postion:/media/joyivan/OLD/data/CT_MD_JPG
#co_cap_Data means the data include post case aka covid-19 and cap case
def creatDir(Dir):
    if not os.path.isdir(Dir):
        os.makedirs(Dir)
def cpDir(source,destinst):
    fileList=os.listdir(source)
    for i in fileList:
        print(i)
        if i[-3:]=='jpg':
            print(source+'/'+i)
            print(destinst+'/')
            shutil.copyfile(source+'/'+i,destinst+'/'+i)

if __name__=='__main__':
    # U can switch on/off using "..." the function below here can generate cap and covid case
    work_dir='/media/joyivan/OLD/data/CT_MD_JPG/'
    print(work_dir+'Index.csv')
    co_cap_Data=pd.read_csv(work_dir+'Index.csv')
    dirList=co_cap_Data['Folder/ID']
    dirList=np.array(dirList)
    for i in dirList:
        if i[0]=='P':
            creatDir(work_dir+'sliceData/covid-19/'+i)
            print('source:'+os.path.join(work_dir, 'COVID-19_Cases', i))
            print('destinst:'+os.path.join(work_dir,'sliceData/covid-19',i))
            cpDir(os.path.join(work_dir,'COVID-19_Cases',i),os.path.join(work_dir,'sliceData/covid-19',i))
        elif i[0]=='c':
            creatDir(work_dir+'sliceData/cap/'+i)
            cpDir(os.path.join(work_dir,'Cap_Cases',i),os.path.join(work_dir,'sliceData/cap',i))
        else :
            print('wrong name')
    # generate normal case
    normalList=os.listdir(os.path.join(work_dir,'Normal_Cases'))
    print(normalList)
    for i in normalList:
        if i[0]=='n':
            creatDir(work_dir+'sliceData/normal/'+i)
            cpDir(os.path.join(work_dir,'Normal_Cases',i),os.path.join(work_dir,'sliceData/normal',i))
