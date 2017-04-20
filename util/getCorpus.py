#!/usr/bin/python3
#coding=utf-8
import os
import os.path
import re
import sys
import json

root = os.path.abspath("..")
rootdir = root+"/corpus/classes"
path = root+"/tmp/"

f = open(root+"/config.json","r")
config = json.load(f)
length = config['length']
f.close()

if len(sys.argv) >= 2:
	rootdir = sys.argv[1]
	print("getCorpus.py update the soruce file!")

index = rootdir.rfind("/")
name = rootdir[index+1:]
print(name)

targetX = path+name+"X.txt"
targetY = path+name+"Y.txt"
if(os.path.exists(targetX)):
	os.remove(targetX)
	os.remove(targetY)
X = open(targetX,'a')
Y = open(targetY,'a')



for root,dirnames,filenames in os.walk(rootdir):
	for file in filenames:
		if file.find('.txt') == -1:
			continue
		print(file)
		f = open(root+"/"+file,'r')
		txt = f.read()
		list = re.findall(r"([\w，、\"\"]*)\[([，。！；：？]|[…]+)\]",txt)
		for l in list:
			if(len(l[0].strip()) == 0):
				continue
			X.write(str(l[0]))
			X.write('\n')
			Y.write(str(l[1]))
			Y.write('\n')
		f.close()
X.close()
Y.close()



