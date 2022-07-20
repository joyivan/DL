import os.path

from PIL import Image
from torch.utils.data import Dataset
from readPickleFile import readFile as rp

dataDir='/home/joyivan/PycharmProjects/pythonProject1/data/cifar-10-batches-py'

class getData(Dataset):
    def __init__(self,fileName,transform=None,flag='train'):
        if flag=='train':
            temp=rp(os.path.join(dataDir,'trainLabel'))
