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
	
max_features = 120000
maxlen = 15  # cut texts after this number of words (among top max_features most common words)
batch_size = 32
path = "/home/chenzewei/GraduationProject/tmp/"

print('Loading data...')
#导入数据
xfile = path+"classes_seg.txt"
yfile = path+"classesY.txt"
xtest = path+"test_seg.txt"
ytest = path+"testY.txt"

X_train = one_hot.one_hot(xfile,n=32000,maxlen=maxlen,split = " ")
y_train = one_hot.one_hot(yfile,n=7,maxlen=maxlen,split = " ")

X_test = one_hot.one_hot(xtest,n=32000,maxlen=maxlen,split = " ")
y_test = one_hot.one_hot(ytest,n=7,maxlen=maxlen,split = " ")


print(len(X_train)," ",len(y_train))

print(len(X_train), 'train sequences')
print('Pad sequences (samples x time)')

X_train = sequence.pad_sequences(X_train,padding='pre',truncating='pre',maxlen=maxlen)
X_test = sequence.pad_sequences(X_test,padding='pre',truncating='pre',maxlen=maxlen)
print('X_train shape:', X_train.shape)
print('X_test shape:', X_test.shape)

print('Build model...')
model = Sequential()
model.add(Embedding(max_features, 128, dropout=0.2))
model.add(LSTM(128, dropout_W=0.2, dropout_U=0.2))  # try using a GRU instead, for fun
model.add(Dense(7))
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


weights = model.get_weights()
np.savetxt(path+"weight.txt",weights)

#。，。？！……
in_test = ["这是 我 心里 最好的 一版 一吻定情",
			"嗯",
			"没有 之一",
			"怎么样 了",
			"你 真棒",
			"等等"
			]
in_test = one_hot.one_hot(in_test,n=32000,maxlen=maxlen,split = " ")
predict = model.predict_classes(in_test, batch_size=32, verbose=1)
print(predict)