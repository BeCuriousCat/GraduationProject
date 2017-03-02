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
path = "/home/chenzewei/GraduationProject/tmp/"
fin = open(path+"json.txt")
json_string = fin.read()
model = model_from_json(json_string)  

model.load_weights(path+'weight.h5') 

maxlen = 15 


in_test = one_hot.replace(path+"in_test.txt")
print(in_test)
in_test = sequence.pad_sequences(in_test,maxlen=15) 
predict = model.predict_classes(in_test, batch_size=32, verbose=1)
print(predict)