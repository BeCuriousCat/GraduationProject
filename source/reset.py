#coding=utf-8
import numpy as np
from numpy import *
import sys
import os
import json
sys.path.append("..")
from keras.preprocessing import sequence,text
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.layers import Embedding
from keras.layers import LSTM
from util import one_hot
from keras.models import model_from_json  

root = os.path.abspath("..")
path = root+"/tmp/"
fin = open(path+"json.txt")
json_string = fin.read()
model = model_from_json(json_string)  

f = open(root+"/config.json","r")
config = json.load(f)
maxlen = config['length']
batch_size = config['batch_size']
wordcnt = config['nb_words']
f.close()

model.load_weights(root+'/weight/weight.h5') 

in_test = one_hot.one_hot(path+"test4_seg.txt",n=wordcnt,maxlen=maxlen,split = " ")
print("[，= 0] [。= 1] [？= 2] [！= 3] ")
in_test = sequence.pad_sequences(in_test,maxlen=maxlen) 
predict = model.predict_classes(in_test, batch_size=batch_size, verbose=1)
set_printoptions(threshold='nan')
print(predict)

