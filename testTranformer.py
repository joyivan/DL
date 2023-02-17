import torch
from torch.utils.data import DataLoader
from torch.utils import data as Data
import torch.nn as nn
import numpy as np

sentences = [['ich mochte ein bier P','S i want a beer .',\
             'i want a beer . E'],\
             ['ich mochte ein cola P','S i want a coke .','i want a \
                                                       coke . E' ]]
src_vocab={'P':0,'ich':1,'mochte':2,'ein':3,'bier':4,'cola':5}
src_vocab_size=len(src_vocab)
tgt_vocab={'P':0,'i':1,'want':2,'a':3,'beer':4,'coke':5,'S':6,'E':7,'.':8}
idx2word={i:w for i ,w in enumerate(tgt_vocab)}
#print (idx2word)
tgt_vocab_size=len(tgt_vocab)

src_len=5
tgt_len=6
def make_date(sentences):
    enc_inputs,dec_inputs,dec_outputs=[],[],[]
    for i in range(len(sentences)):
        enc_input=[[src_vocab[n] for n in sentences[i][0].split()]]
        dec_input=[[tgt_vocab[n] for n in sentences[i][1].split()]]
        dec_output=[[tgt_vocab[n] for n in sentences[i][2].split()]]

        enc_inputs.extend(enc_input)
        dec_inputs.extend(dec_input)
        dec_outputs.extend(dec_output)
    return torch.LongTensor(enc_inputs),torch.LongTensor(dec_inputs),torch.LongTensor(dec_inputs)
enc_inputs,dec_inputs,dec_outputs=make_date(sentences)
class MydataSet(Data.Dataset):
    def __init__(self,enc_inputs,dec_inputs,dec_outputs):
        super(MydataSet,self).__init__()
        self.enc_inputs=enc_inputs
        self.dec_inputs=dec_inputs
        self.dec_outputs=dec_outputs

    def __len__(self):
        return enc_inputs.shape[0]

    def __getitem__(self, item):
        return self.enc_inputs[item],dec_inputs[item],self.dec_outputs[item]
loader= Data.DataLoader(MydataSet(enc_inputs,dec_inputs,dec_outputs),2,True)

d_model = 512
d_ff=2048
d_k=d_v=64
n_layers=6
n_heads=8
def get_sinusoid_encoding_table(n_position,d_model):
    def cal_angle(postion,hid_idx):
        return postion/np.power(10000,2*(hid_idx//2)/d_model)
    def get_posi_angle_vec(position):
        return [cal_angle(position,hid_j) for hid_j in range(d_model)]

    sinusoid_table=np.array([get_posi_angle_vec(pos_i) for pos_i in range(n_position)])
    sinusoid_table[:,0::2]=np.sin(sinusoid_table[:,0::2])
    sinusoid_table[:,1::2]=np.cos(sinusoid_table[:,1::2])
    return sinusoid_table
def get_attn_pad_mask(seq_q,seq_k):
    batch_size,len_q=seq_q.size()
    batch_size,len_k=seq_k.size()

    pad_attn_mask = seq_k.data.eq(0).unsqueeze(1)
    return pad_attn_mask.expand(batch_size,len_q,len_k)



def get_attn_subsequence_mask(seq):
    attn_shape=[seq.size(0),seq.size(1),seq.size(1)]
    subsequence_mask=np.triu(np.ones(attn_shape),k=1)
    subsequence_mask=torch.from_numpy(subsequence_mask).byte()
    return subsequence_mask

def ScaledDotProductAttention(nn.Module):
    def __init__(self):
        super(ScaledDotProductAttention,self).__init__()

    def foward(self,Q,K,V,attn_mask):
        '''

        :param self:
        :param Q: [batch size,n_heads,len_q,d_k]
        :param K: [batch size,n_heads,len_k,d_k]
        :param V:
        :param attn_mask:
        :return:
        '''
        scores=torch.matmul(Q,K.transpose(-1,-2))/np.sqrt(d_k)
        scores.masked_fill_(attn_mask,-1e9)

        attn=nn.Softmax(dim=-1)(scores)
        context=torch.matmul(attn,V)
        return context,attn

class MultiHeadAttention(nn.Module):
    def __init__(self):
        super(MultiHeadAttention,self).__init__()
        self.W_Q=nn.Linear(d_model,d_k*n_heads,bias=False)
        self.W_K=nn.Linear(d_model,d_k*n_heads,bias=False)
        self.W_V=nn.Linear(d_model,d_k*n_heads,bias=False)
    def foward(self,input_Q,input_K,input_V,attn_mask):
        '''

        :param input_Q:[batch_size,len_q,d_model]
        :param input_K:
        :param input_V:[batch_size,len_v,d_model]
        :param attn_mask:[batch_size,seq_len,seq_len]
        :return:
        '''

        residual,batch_size=input_Q,input_Q.size(0)


