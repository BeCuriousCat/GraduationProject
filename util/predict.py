#!/usr/bin/python
#coding=utf-8
from __future__ import print_function

import re
import jieba
import os
import json
from util import one_hot


def getCorpus(txt):
	print("get Corpus")
	X = []
	list = re.findall(r"([\w，、\"\"]*)\[([，。！；：？]|[…]+)\]",txt)
	print(list)
	for l in list:
		if(len(l[0].strip()) == 0):
			continue
		print(l)
		X.append(str(l[0]))
	return X

def segment(list):
	print("segment")
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
	result = []
	root = os.path.abspath(".")
	path = root+"/tmp/"
	fin = open(path+"json.txt")
	f = open(root+"/config.json","r")
	config = json.load(f)
	maxlen = config['length']
	wordcnt = config['nb_words']
	puct = config['punctuation']
	batch_size = config['batch_size']
	f.close()
	#分词
	seglist = segment(list)
	print(seglist)
	json_string = fin.read()
	fin.close()
	model = model_from_json(json_string)
	model.load_weights(root+'/weight/weight.h5') 
	#one hot encode 
	onehotlist = one_hot.one_hot4Line(seglist,n=wordcnt,maxlen=maxlen,split=" ")
	#padding

	inTxt = sequence.pad_sequences(onehotlist,maxlen=maxlen) 
	predictNo = model.predict_classes(inTxt, batch_size=batch_size, verbose=1)
	for i in range(0,len(inTxt)):
		predict = puct[int(predictNo[i])]
		result.append(list[i]+"["+predict+"]")
	return result
