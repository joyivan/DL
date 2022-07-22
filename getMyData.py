import os.path

from PIL import Image
from torch.utils.data import Dataset
from readPickleFile import readFile as rp
from torchvision import transforms

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
                                               transforms.Normalize((0.5,0.5,0.5),(0.5,0.5,0.5))])
            self.flag=flag
    def __len__(self):
        return len(self.temp)
    def __getitem__(self, index):
        imgName=self.temp[index][0]
        imgLabel = self.temp[index][1]
        img=Image.open(os.path.join(dataDir),imgName)
        imgTensor=self.transform(img)
        retrun imgTensor,imgLabel
