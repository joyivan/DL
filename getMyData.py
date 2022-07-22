import os.path

from PIL import Image
from torch.utils.data import Dataset
from readPickleFile import readFile as rp
from torchvision import transforms
'''

[tensor(0.4478, device='cuda:0', dtype=torch.float64), tensor(0.4835, device='cuda:0', dtype=torch.float64), tensor(0.4921, device='cuda:0', dtype=torch.float64)]
[tensor(0.2627, device='cuda:0', dtype=torch.float64), tensor(0.2438, device='cuda:0', dtype=torch.float64), tensor(0.2468, device='cuda:0', dtype=torch.float64)]
mean and std value which was using 10000 images .
the image that be readed by PIL is RGB mode, cv2 is BGR mode.
'''
dataDir='/home/joyivan/PycharmProjects/pythonProject1/data/cifar-10-batches-py'

class getData(Dataset):
    def __init__(self,transform=None,flag='train'):
        if flag=='train':
            self.temp=rp(os.path.join(dataDir,'trainData'))
        else:
            self.temp=rp(os.path.join(dataDir,'validDate'))
        if not transform==None:
            self.transform=transform
        else:
            self.transform=transforms.Compose([transforms.ToTensor(),
                                               transforms.Normalize((0.4478,0.4835,0.4921),(0.2627,0.2438,0.2468))])
            self.flag=flag
    def __len__(self):
        return len(self.temp)
    def __getitem__(self, index):
        imgName=self.temp[0][index]
        imgLabel = self.temp[1][index]
        print(os.path.join(dataDir, self.flag, imgName))
        img=Image.open(os.path.join(dataDir,self.flag,imgName),'r')
        imgTensor=self.transform(img)
        return imgTensor,imgLabel
