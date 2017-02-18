#!/usr/bin/python3.5
import jieba 

fin = open('../corpus/The_three_body_x.txt','r')
fou = open('../corpus/The_three_body_seg.txt','w')

line = fin.readline()
while line:
	newline = jieba.cut(line,cut_all=False) 
	str_out = " ".join(newline)
	print(str_out),
	print(str_out,file=fou),		
	line = fin.readline()

fin.close()
fou.close()