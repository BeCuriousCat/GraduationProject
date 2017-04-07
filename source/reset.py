import numpy as np
import sys
sys.path.append("..")
np.random.seed(1337)
from keras.preprocessing import sequence,text
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.layers import Embedding
from keras.layers import LSTM
from util import one_hot
from keras.models import model_from_json  

path = "/home/ccit/chenzewei/GraduationProject/tmp/"
fin = open(path+"json.txt")
json_string = fin.read()
model = model_from_json(json_string)  
model.load_weights('/home/ccit/chenzewei/GraduationProject/weight/weight.h5') 
maxlen = 10 
in_test = one_hot.one_hot(path+"predict.txt",n=114120,maxlen=maxlen,split = " ")

in_test = sequence.pad_sequences(in_test,maxlen=10) 
predict = model.predict_classes(in_test, batch_size=32, verbose=1)
print predict


