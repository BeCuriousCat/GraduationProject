#!/usr/bin/python3.5
#coding=utf-8
import re
import jieba
import os

def getCorpus(txt):	
	X = []
	list = re.findall(r"([\w，、\"\"]*)\[([，。！；：？]|[…]+)\]",txt)
	for l in list:
		if(len(l[0].strip()) == 0):
			continue	
		X.append(str(l[0]))
	return X

def segment(list):
	X = [] 
	for i in list:
		newline = jieba.cut(i,cut_all=False)
		str_out = " ".join(newline)
		X.append(str_out)
	return X


from keras.preprocessing import sequence,text
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.layers import Embedding
from keras.layers import LSTM
from keras.models import model_from_json  

def predict(list):
	root = os.path.abspath("..")
	fin = open(root+"/tmp/json.txt")

	f = open(root+"/config.json","r")
	config = json.load(f)
	maxlen = config['length']
	wordcnt = config['nb_words']
	f.close()

	json_string = fin.read()
	model = model_from_json(json_string)
	model.load_weights(root+'/weight/weight.h5') 

	
	in_test = sequence.pad_sequences(list,maxlen=maxlen) 
	predict = model.predict_classes(in_test, batch_size=batch_size, verbose=1)
	set_printoptions(threshold='nan')
	print(predict)
