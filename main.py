import torch
import torch.nn as nn
import torch.optim as optim
from torch.optim import lr_scheduler
import numpy as np
import torchvision
from torchvision import datasets, models, transforms
import matplotlib.pyplot as plt
import time
import os
import copy

mean = np.array([0.5, 0.5, 0.5])
std = np.array([0.25, 0.25, 0.25])
data_transformer = {
    'train': transforms.Compose([
        transforms.RandomResizedCrop(224),
        transforms.RandomHorizontalFlip(),
        transforms.ToTensor(),
        transforms.Normalize(mean, std)
    ]),
    'val': transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean, std)
    ]),
}
data_dir='/media/joyivan/7699af0c-97b8-41e3-abd7-e0aa90990d22/joyivan/data/lung'
cur_dir=os.path.abspath(os.path.join(data_dir,'negative'))
print(cur_dir)
file_list=os.listdir(cur_dir)
print(file_list)
#image_datasets ={x:datasets.ImageFolder(os.path.abspath(os.path.join(data_dir,x))) for x in ['negative','positive']}
image_datasets =datasets.ImageFolder(data_dir,transform=data_transformer['val'])
dataloaders = torch.utils.data.DataLoader(image_datasets, batch_size=4,
                                             shuffle=True, num_workers=0)
inputs, classes = next(iter(dataloaders))
print(inputs.shape)
def imshow(inp, title):
    """Imshow for Tensor."""
    inp = inp.numpy().transpose((1, 2, 0))
    inp = std * inp + mean
    inp = np.clip(inp, 0, 1)
    plt.imshow(inp)
    plt.title(title)
    plt.show()
plt.imshow(inputs[0][0])
plt.show()
