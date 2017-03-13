import numpy as np
import sys
sys.path.append("..")
from keras.preprocessing import sequence,text
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.layers import Embedding
from keras.layers import LSTM
from util import one_hot
from keras.models import model_from_json  
from keras.utils.visualize_util import plot
path = "/home/chenzewei/GraduationProject/tmp/"
fin = open(path+"json.txt")
json_string = fin.read()
model = model_from_json(json_string)  
plot(model, to_file='model1.png', show_shapes=True)
model.load_weights(path+'weight.h5') 
plot(model, to_file='model.png', show_shapes=True)
maxlen = 15 


in_test = one_hot.one_hot(path+"in_test.txt",n=32000,maxlen = maxlen)
print(in_test)
in_test = sequence.pad_sequences(in_test,maxlen=15) 
predict = model.predict_classes(in_test, batch_size=32, verbose=1)
print(predict)

x_test = one_hot.one_hot(path+"test2_seg.txt",n=32000,maxlen=maxlen,split = " ")
y_test = one_hot.replace(path+"test2Y.txt")
