import torch

sentences = [['ich mochte ein bier P','S i want a beer .',\
             'i wante a beear . E'],\
             ['ich mochte ein cola P','S i want a coke .','i want a \
                                                       coke . E' ]]
src_vocab={'P':0,'ich':1,'mochte':2,'ein':3,'bier':4,'cola':5}
src_vocab_size=len(src_vocab)
tgt_vocab={'P':0,'i':1,'want':2,'a':3,'bear':4,'coke':5,'S':6,'E':7,'.':8}
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
enc_inputs,dec_inputs,dec_outpus=make_date(sentences)
class MydataSet(Data.Dataset):
    def __init__(self,enc_inputs,dec_inputs,dec_outs):
        super(MydataSet,self).__init__()
        self.enc_inputs=enc_inputs
        self.dec_inputs=dec_inputs
        self.dec_outputs=dec_outs

    def
