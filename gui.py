#!/usr/bin/python3.5
#coding=utf-8

import tkinter.filedialog
import json
import os
from tkinter import * 
from appJar import gui
from util import predict,one_hot



def openFun(self):
	fn=tkinter.filedialog.askopenfilename(title='选择一个文件', filetypes=[('所有文件','.*'),('文本文件','.txt')])
	f = open(fn)
	text = f.read()
	f.close()
	app.setTextArea("t1",text=text)

def saveFun(self):
	print('save')

def saveAsFun(self):
	print('save as...')

def run(self):
	text = app.getTextArea("t1")
	original = predict.getCorpus(text)
	segment = predict.segment(original)
	#one hot encode should be complete in the predict()
	result = predict.predict(list)
	app.setTextArea("t2",onehot)
	

global app
global wordcnt,maxlen

root = os.path.abspath(".")
f = open(root+"/config.json","r")
config = json.load(f)
maxlen = config['length']
wordcnt = config['nb_words']
f.close()

app=gui("中文标点审校","500x400")
app.setStretch("both")
app.setSticky("nesw") 
app.setFont(14)
app.addScrolledTextArea("t1",0,0,1,1)
app.addScrolledTextArea("t2",0,1,1,1)

app.addMenuItem("File", "open", openFun)
app.addMenuItem("File", "-")
app.addMenuItem("Edit", "run",run)
app.addMenuItem("File", "save", saveFun)
app.addMenuItem("File", "save as...", saveAsFun)


app.go()
