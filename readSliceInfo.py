import pydicom
import argparse
import os
import glob

work_dir='/media/joyivan/OLD/data/CT_MD_JPG/'

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-workDIR', type=str, default=work_dir, help='gl')
    parser.add_argument('-orginDIR', type=str, default='COVID-19_Cases', help='gl')
    opt = parser.parse_args()
    print(opt)

    workDIR = os.path.join(opt.workDIR, opt.orginDIR)
    print(workDIR)
    for root, dirs, files in os.walk(workDIR):
        for dir in dirs:
            dimList = glob.glob(os.path.join(root, dir, '*.dcm'))
            print('dir is ', dir)
            sliceLocationFileNameList=[]
            slicelocationList=[]
            for i in dimList:
            # print(dimList)
                fileInfo=pydicom.read_file(i)
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
                print(f'dir is {pat1},filename is {file}')
                os.rename(fileName,part1+'/check'+"IM"+str(fileNo).zfill(4)+'.jpg')
                fileNo+=1
            print(dir+'rename files:'+str(fileNo))