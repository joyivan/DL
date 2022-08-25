import pydicom
work_dir='/media/joyivan/OLD/data/CT_MD_JPG'
orginDIR='COVID-19_Cases'
data0=pydicom.read_file(work_dir+'/'+orginDIR+'/P073/'+'IM0144.dcm')
data1=pydicom.dcmread(work_dir+'/'+orginDIR+'/P073/'+'IM0144.dcm')
print(data0[0x0020,0x1041].value)