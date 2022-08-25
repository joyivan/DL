import argparse
import os
import glob
#rename drop check String in filename
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
            jpgList = glob.glob(os.path.join(root, dir, '*.jpg'))
            print('dir is ', dir)
            for i in jpgList:
                part1,part2=os.path.split(i)
                if part2[:5]=='check':
                    print(part1,part2)
                    os.rename(i,part1+'/'+part2[5:])