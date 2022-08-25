import os
from pydicom import dcmread      #用于读取DICOM(DCOM)文件
import pylibjpeg
import argparse
import imageio
import glob
import numpy as np
from PIL import Image
import dicom2jpg
import shutil
import datetime

def d2j2(fileName):
    basePart,filePart=os.path.split(fileName)
    print(basePart)
    dicom2jpg.dicom2jpg(i,target_root=basePart,anonymous=False,multiprocessing=True)
    print(filePart+'over')
def d2j(fileName):
    temp=dcmread(fileName)
    img=temp.pixel_array.astype(float)
    rescaled_image =(np.maximum(img,0)/img.max())*255
    img=np.uint8(rescaled_image)
    img=Image.fromarray(img)
    basePart,filePart=os.path.split(fileName)
    file,ex=filePart.split('.') 
    newFile=os.path.join(basePart,file+'.jpg')
    print(newFile)
    imageio.imwrite(newFile,img) 
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-baseDIR', type=str, default='f:\COVID-19\CT_MD', help='gl')
    parser.add_argument('-orginDIR', type=str, default='Cap_Cases', help='gl')
    parser.add_argument('-destDIR', type=str, default='Cap_ Cases', help='gl')
    opt=parser.parse_args()
    print(opt)
    
    os.chdir(os.path.join(opt.baseDIR,opt.orginDIR))
    workDIR=os.path.join(opt.baseDIR,opt.orginDIR)
    print (workDIR)
    for root,dirs,files in os.walk(workDIR):
        for dir in dirs: 
            dimList=glob.glob(os.path.join(root,dir,'*.dcm'))
            print('dir is ',dir)
            for i in dimList:
                d2j2(i)
            #print(dimList)

            jpgList=glob.glob(os.path.join(root,dir,datetime.datetime.now().strftime('%Y%m%d'),\
               dir+'_jpg','__CT_','*.jpg'))
            print(jpgList)
             
            for j in jpgList:
                shutil.move(j,os.path.join(root,dir))
            _jpgList=glob.glob(os.path.join(root,dir,'*.jpg'))
            #stk_code =1
            #stk_code = str(stk_code).zfill(6)
            print(_jpgList)
            for k in _jpgList:
                digiPart=os.path.split(k)[1][5:].split('.')[0].zfill(4)
                os.rename(k,os.path.join(root,dir,'IM'+digiPart+'.jpg')) 
