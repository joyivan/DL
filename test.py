import pydicom
import numpy as np
work_dir='/media/joyivan/OLD/data/CT_MD_JPG'
orginDIR='Cap_Cases'
data0=pydicom.read_file(work_dir+'/'+orginDIR+'/cap003/'+'checkedIM0134.dcm')
data1=pydicom.dcmread(work_dir+'/'+orginDIR+'/cap003/'+'checkedIM0134.dcm')
print(data0)
print(data0[0x0020,0x1041].value)
pixArray=np.array(data0.pixel_array)
print(np.max(pixArray))
from playsound import playsound
playsound("/home/joyivan/Downloads/non.mp3")