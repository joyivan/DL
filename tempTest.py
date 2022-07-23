import torch
from torch.autograd import Variable
a=Variable(torch.FloatTensor([[2.,4.]]),requires_grad=True)
b=torch.zeros(1,2)
b[0,0]=a[0,0]**2+a[0,1]
b[0,1]=a[0,1]**3+a[0,0]
out=b*2
out.backward(torch.FloatTensor([[1.,1.]]))
print(out)
print(a)
print(a.grad)
