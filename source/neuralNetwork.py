#!/usr/bin/python3.5
#codeing utf-8
import numpy as np
import sys
sys.path.append("..")
np.random.seed(1337)

from keras.preprocessing import sequence,text
from keras.models import Sequential
from keras.layers import Dense,Activation,Embedding
from keras.layers import LSTM
from util import one_hot
	
max_features = 148144
maxlen = 6  # cut texts after this number of words (among top max_features most common words)
batch_size = 32
path = "/home/chenzewei/GraduationProject/corpus/"

print('Loading data...')
#导入数据
xfile = path+"The_three_body_seg.txt"
yfile = path+"The_three_body_replace_y.txt"
xtest = path+"test_seg.txt"
ytest = path+"test_replace_y.txt"

X_train = one_hot.one_hot(xfile,n=32000,maxlen=maxlen,split = " ")
y_train = one_hot.one_hot(yfile,n=17,maxlen=maxlen,split = " ")
X_test = one_hot.one_hot(xtest,n=857,maxlen=maxlen,split = " ")
y_test = one_hot.one_hot(ytest,n=17,maxlen=maxlen,split = " ")


print(len(X_train)," ",len(y_train))
ftx = open("/home/chenzewei/GraduationProject/tmp/X_sequence.txt",'w')
ftx2 = open("/home/chenzewei/GraduationProject/tmp/X_sequence2.txt",'w+')
fty = open("/home/chenzewei/GraduationProject/tmp/Y_sequence.txt",'w')
print(X_train,file=ftx)
print(y_train,file=fty)
print(len(X_train), 'train sequences')
print('Pad sequences (samples x time)')
X_train = sequence.pad_sequences(X_train,padding='pre',truncating='pre',maxlen=maxlen)
X_test = sequence.pad_sequences(X_test, maxlen=maxlen)
print('X_train shape:', X_train.shape)
print('X_test shape:', X_test.shape)
print(X_train,file = ftx2)

print('Build model...')
model = Sequential()
model.add(Embedding(max_features, 128, dropout=0.2))
model.add(LSTM(128, dropout_W=0.2, dropout_U=0.2))  # try using a GRU instead, for fun
model.add(Dense(17))
model.add(Activation('softmax'))

# try using different optimizers and different optimizer configs
model.compile(loss='sparse_categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

print('Train...')
model.fit(X_train, y_train, batch_size=batch_size, nb_epoch=15)
score, acc = model.evaluate(X_test, y_test,batch_size=batch_size)
print('Test score:', score)
print('Test accuracy:', acc)

