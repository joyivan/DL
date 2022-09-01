import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import math,copy,time
from torch.autograd import Variable
import matplotlib.pyplot as plt
import seaborn
# http://nlp.seas.harvard.edu/2018/04/03/attention.html
#
seaborn.set_context(context="talk")

class EncoderDecoder(nn.Module):
    def __init__(self,encoder,decoder,src_embed,tgt_embed,generator):
        super(EncoderDecoder,self).__init__()
        self.encoder =encoder
        self.decoder = decoder
        self.src_embed= src_embed
        self.tgt_embed = tgt_embed
        self.generator=generator

    def forward(self,src,tgt,src_mask,tgt_mask):
        return self.decoder(self.encoder)


