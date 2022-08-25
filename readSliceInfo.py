import pydicom
workDIR='f:\COVID-19\CT_MD'
orginDIR='COVID-19_Cases'
data0=pydicom.read_file(workDIR+'\\'+orginDIR+'\\P001\\'+'IM0004.dcm')
data1=pydicom.dcmread(workDIR+'\\'+orginDIR+'\\P001\\'+'IM0004.dcm')
print(data0)
print('-'*70)
print(data1)
