#!/usr/bin/python3.5
#coding=utf-8
from __future__ import absolute_import 
from __future__ import print_function
import numpy as np
import sys
sys.path.append("..")
np.random.seed(1337)

from keras.preprocessing import sequence,text
from keras.models import Sequential
from keras.layers import Dense,Activation,Embedding
from keras.layers import LSTM
from util import one_hot
import os
import json

#config数据
root = os.path.abspath("..")
f = open(root+"/config.json","r")
config = json.load(f)
maxlen = config['length']
max_features =config['max_features']
batch_size = config['batch_size']
wordcnt = config['nb_words']
targer = config['targer']
flist = config['filelist']
dropout = config['dropout']
prd_size = config['predict_size']
f.close()

path = root+"/tmp/"

#max_features = 120000
#maxlen = 10  # cut texts after this number of words (among top max_features most common words)
#batch_size = 32

print('Loading data...')
#导入数据
xfile = path+"classes_seg.txt"
yfile = path+"classesY.txt"

X_train = one_hot.one_hot(xfile,n=wordcnt,maxlen=maxlen,split = " ")
y_train = one_hot.replace(yfile)

files = flist
y_target = targer
x_t = []
y_t = []
x_test = []
y_test = []
for i in range(0, len(files)):
	x_t.append(path+files[i]+"_seg.txt")
	y_t.append(path+files[i]+"Y.txt")
	x_test.append(one_hot.one_hot(x_t[i],n=wordcnt,maxlen=maxlen,split = " "))
	y_test.append(one_hot.replace(y_t[i]))


print(len(X_train)," ",len(y_train))

print(len(X_train), 'train sequences')
print('Pad sequences (samples x time)')

X_train = sequence.pad_sequences(X_train,padding='pre',truncating='pre',maxlen=maxlen)

for i in range(0, len(files)):
	x_test[i] = sequence.pad_sequences(x_test[i],padding='pre',truncating='pre',maxlen=maxlen)
	print('X_test ',i,' shape:', x_test[i].shape)

print('X_train shape:', X_train.shape)


print('Build model...')
model = Sequential()
model.add(Embedding(max_features, 128, dropout=dropout))
model.add(LSTM(128, dropout_W=dropout, dropout_U=dropout))  # try using a GRU instead, for fun
model.add(Dense(prd_size))
model.add(Activation('softmax'))

# try using different optimizers and different optimizer configs
model.compile(loss='sparse_categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

print('Train...')
model.fit(X_train, y_train, batch_size=batch_size, nb_epoch=15,verbose=1)

print("save the weight")
filepath = "../weight/weight.h5"
model.save_weights(filepath)

for i in range(0, len(files)):
	print(y_target[i],"检测结果")
	score, acc = model.evaluate(x_test[i], y_test[i],batch_size=batch_size)
	print('Test score:', score)
	print('Test accuracy:', acc)



json_string = model.to_json() 
json = open(path+'json.txt','w')
print(json_string,file=json)

prend = one_hot.one_hot(path+"test2_seg.txt",n=wordcnt,maxlen=maxlen,split = " ")
predict = model.predict_classes(prend, batch_size=32, verbose=1)
print(predict)
