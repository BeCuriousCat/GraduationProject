#!/usr/bin/python
#coding=utf-8


import json
import os
import tkinter 
from appJar import gui
from util import predict,one_hot



def openFile(self):
	fn=tkinter.filedialog.askopenfilename(title='选择一个文件', filetypes=[('所有文件','.*'),('文本文件','.txt')])
	f = open(fn)
	text = f.read()
	f.close()
	app.setTextArea("t1",text=text)

def saveFile(self):
	print('save')

def saveAsFile(self):
	print('save as...')

def run(self):
	text = app.getTextArea("t1")
	original = predict.getCorpus(text)
	#segment,one hot encode should be complete in the predict()
	result = predict.predict(original)
	app.setTextArea("t2",result)
	

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

app.addMenuItem("File", "open", openFile)
app.addMenuItem("File", "-")
app.addMenuItem("Edit", "run",run)
app.addMenuItem("File", "save", saveFile)
app.addMenuItem("File", "save as...", saveAsFile)


app.go()

