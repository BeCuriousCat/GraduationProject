#coding=utf-8
from __future__ import print_function
def one_hot(fName,n,maxlen,split=" "):
	fin = open(fName,'r')
	seq = []
	line = fin.readline()

	while line:
		line = line.strip(' \n').split(split)
		intege = [(abs(hash(w)) % (n - 1) + 1) for w in line]
		seq.append(intege)
		line = fin.readline()

	return seq

def replace(fName):
	fin = open(fName,'r')
	seq = []
	line = fin.readline()
	a = ['，','。','？','！']
	while line:
		line = line.strip(' \n')
		intege = a.index(line)
		seq.append(intege)
		line = fin.readline()
	return seq

def one_hot4Line(array,n,maxlen,split=" "):
	seq = []
	for line in array:
		line = line.strip(' \n').split(split)
		intege = [(abs(hash(w)) % (n - 1) + 1) for w in line]
		seq.append(intege)
	return seq
	
