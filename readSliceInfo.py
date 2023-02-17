import pydicom
import argparse
import os
import glob
from playsound import playsound


#sort jpg from dicom information
work_dir='/media/joyivan/OLD/data/CT_MD_DCM/'

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-workDIR', type=str, default=work_dir, help='gl')
    #COVID-19 Cap Normal
    parser.add_argument('-orginDIR', type=str, default='Normal_Cases', help='gl')
    opt = parser.parse_args()
    print(opt)

    workDIR = os.path.join(opt.workDIR, opt.orginDIR)
    print(workDIR)
    for root, dirs, files in os.walk(workDIR):
        for dir in dirs:
            #fileNameList
            dimList = glob.glob(os.path.join(root, dir, '*.dcm'))
            print('dir is ', dir)
            #a dictonary to get fileName and the location in the same file (location:fileName)
            sliceLocationFileNameList=[]
            slicelocationList=[]
            for i in dimList:
            # print(dimList)
                fileInfo=pydicom.read_file(i)
            #get silceLocation Imformation
                sliceLocation=fileInfo[0x0020,0x1041].value
                sliceLocation=float(sliceLocation)
                sliceLocationFileNameList.append((sliceLocation,i))
                slicelocationList.append(sliceLocation)

            #print(sliceLocationFileNameList)
            #get kv k:sliceLocation v:fileName
            sliceLocationFileNameListDict=dict((sliceLocationFileNameList))
            #print(sliceLocationFileNameListDict)
            slicelocationList=sorted(slicelocationList,reverse = True )
            #print(slicelocationList)
            fileNo=1
            for j in slicelocationList:
                #print("sliceList:"+str(j))
                #print(sliceLocationFileNameListDict)

                fileName=sliceLocationFileNameListDict[j]
                part1,file=os.path.split(str(fileName))
                #print("result:"+file)
                print(f'dir is {part1},filename is {file}')
                #the code blow can rename jpg file to fixed sorted name
                #os.rename(fileName[:-4]+'.jpg',part1+'/check'+"IM"+str(fileNo).zfill(4)+'.jpg')
                os.rename(fileName,part1+'/checked'+"IM"+str(fileNo).zfill(4)+'.dcm')
                fileNo+=1
            print(dir+'rename files:'+str(fileNo-1))

    playsound("/home/joyivan/Downloads/non.mp3")
''' 
    for root, dirs, files in os.walk(workDIR):
        for dir in dirs:
            jpgList = glob.glob(os.path.join(root, dir, '*.jpg'))
            for i in jpgList:
                print(jpgList)
 '''