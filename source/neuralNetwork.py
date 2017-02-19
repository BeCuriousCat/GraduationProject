#!/usr/bin/python3.5
#codeing utf-8
import numpy as np
np.random.seed(1337)

from keras.preprocessing import sequence,text
from keras.models import Sequential
from keras.layers import Dense,Activation,Embedding
from keras.layers import LSTM

	
max_features = 20000
maxlen = 80  # cut texts after this number of words (among top max_features most common words)
batch_size = 32
path = "/home/chenzewei/GraduationProject/corpus/"

print('Loading data...')
#导入数据
t = open(path+"The_three_body_replace_y.txt")
alltxt = t.read()
#y = text.one_hot(alltxt,44,lower=True,filters='!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n',split=" ")
#X_train = open(path+"The_three_body_replace_x.txt").read()
#X_train = text.text_to_word_sequence(X_train,lower=True, split=" ")
#X_train = text.text_to_word_sequence(X_train,32000,filters='!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n',lower=True)
file = open('/home/chenzewei/tmp_X.txt','w')
print(X_train,file=file)
file.close()
y_train = y
print(X_train)
print(len(X_train)," ",len(y))
print(len(X_train), 'train sequences')
# print('Pad sequences (samples x time)')
# X_train = sequence.pad_sequences(X_train, maxlen=maxlen)
# X_test = sequence.pad_sequences(X_test, maxlen=maxlen)
# print('X_train shape:', X_train.shape)
# print('X_test shape:', X_test.shape)

print('Build model...')
model = Sequential()
model.add(Embedding(max_features, 128, dropout=0.2))
model.add(LSTM(128, dropout_W=0.2, dropout_U=0.2))  # try using a GRU instead, for fun
model.add(Dense(1))
model.add(Activation('softmax'))

# try using different optimizers and different optimizer configs
model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

print('Train...')
model.fit(X_train, y_train, batch_size=batch_size, nb_epoch=15)
# score, acc = model.evaluate(X_test, y_test,batch_size=batch_size)
# print('Test score:', score)
# print('Test accuracy:', acc)

