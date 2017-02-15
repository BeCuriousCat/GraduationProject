#coding utf-8

import jieba 

fin = open('../corpus/The_three_body.txt'.'r')
fou = open('../corpus/The_three_body_seg.txt','w')

lin = fin.readline()
while line:
	newline = jieba.cut(line,cut_all=False) #精簡模式
	str_out = ' '.jion(newline).encode('utf-8')
	print srt_out,
	print >> fou,str_out,
	line = fin.readline()

fin.close()
fou.close()