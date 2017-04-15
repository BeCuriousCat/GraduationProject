#!/usr/bin/python3.5
import jieba
import sys

path = "../corpus/"
name = "test"
if len(sys.argv) >= 2:
	name = sys.argv[1]
	path = sys.argv[2]

print("segment the file :"+name)

fin = open(path+name+"X.txt",'r')
fou = open(path+name+'_seg.txt','w')

line = fin.readline()
while line:
	newline = jieba.cut(line,cut_all=False) 
	str_out = " ".join(newline)
	str_out = str_out.replace(r"\n","")
	#print(str_out,end=""),
	print(str_out,file=fou,end=""),
	line = fin.readline()

fin.close()
fou.close()