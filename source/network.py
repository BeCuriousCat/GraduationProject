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
from keras.utils.visualize_util import plot
#需要修改
path = "/home/chenzewei/GraduationProject/tmp/"

max_features = 120000
maxlen = 10  # cut texts after this number of words (among top max_features most common words)
batch_size = 32

print('Loading data...')
#导入数据
xfile = path+"classes_seg.txt"
yfile = path+"classesY.txt"

X_train = one_hot.one_hot(xfile,n=40000,maxlen=maxlen,split = " ")
y_train = one_hot.replace(yfile)

files = ["test","test2","test3","test4","test5"]
y_target = ["综合","，","！","。","？"]
x_t = []
y_t = []
x_test = []
y_test = []
for i in range(0, len(files)):
	x_t.append(path+files[i]+"_seg.txt")
	y_t.append(path+files[i]+"Y.txt")
	x_test.append(one_hot.one_hot(x_t[i],n=40000,maxlen=maxlen,split = " "))
	y_test.append(one_hot.replace(y_t[i]))


# X_test = one_hot.one_hot(xtest,n=32000,maxlen=maxlen,split = " ")
# y_test = one_hot.one_hot(ytest,n=7,maxlen=maxlen,split = " ")


print(len(X_train)," ",len(y_train))

print(len(X_train), 'train sequences')
print('Pad sequences (samples x time)')

X_train = sequence.pad_sequences(X_train,padding='pre',truncating='pre',maxlen=maxlen)

for i in range(0, len(files)):
	x_test[i] = sequence.pad_sequences(x_test[i],padding='pre',truncating='pre',maxlen=maxlen)
	print('X_test ',i,' shape:', x_test[i].shape)
# X_test = sequence.pad_sequences(X_test,padding='pre',truncating='pre',maxlen=maxlen)
print('X_train shape:', X_train.shape)


print('Build model...')
model = Sequential()
model.add(Embedding(max_features, 128, dropout=0.2))
model.add(LSTM(128, dropout_W=0.2, dropout_U=0.2))  # try using a GRU instead, for fun
model.add(Dense(4))
model.add(Activation('softmax'))

# try using different optimizers and different optimizer configs
model.compile(loss='sparse_categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

print('Train...')
model.fit(X_train, y_train, batch_size=batch_size, nb_epoch=15,verbose=1)

for i in range(0, len(files)):
	print(y_target[i],"检测结果")
	score, acc = model.evaluate(x_test[i], y_test[i],batch_size=batch_size)
	print('Test score:', score)
	print('Test accuracy:', acc)

filepath = "../weight/weight.h5"
model.save_weights(filepath)

json_string = model.to_json() 
json = open(path+'json.txt','w')
print(json_string,file=json)

predict = model.predict_classes("../tmp/test2_seg.txt", batch_size=32, verbose=1)
print(predict)
