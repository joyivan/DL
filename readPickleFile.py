import pickle
def readFile(file):
    with open(file,'rb') as fo:
        dict_=pickle.load(fo,encoding="bytes")
    return dict_