#!/usr/bin/python
# -*- coding: UTF-8 -*- 

import re

fin  = open('../corpus/The_three_body.txt','r')
foux = open('../corpus/X_train.txt','w')
fouy = open('../corpus/Y_train.txt','w')

line = fin.readline()

pattern = ur"\p{P}"
while line:
	line = line.decode('utf-8')
	print(line)
	list = re.findall(pattern, line)
	line = fin.readline()



