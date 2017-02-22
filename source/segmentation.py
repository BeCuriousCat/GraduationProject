#!/usr/bin/python3.5
import jieba 

name = "test"
fin = open('../corpus/'+name+'_replace_x.txt','r')
fou = open('../corpus/'+name+'_seg.txt','w')

line = fin.readline()
while line:
	newline = jieba.cut(line,cut_all=False) 
	str_out = " ".join(newline)
	str_out = str_out.replace(r"\n","")
	print(str_out,end=""),
	print(str_out,file=fou,end=""),
	line = fin.readline()

fin.close()
fou.close()