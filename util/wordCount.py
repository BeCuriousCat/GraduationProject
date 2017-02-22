#!/usr/bin/python3.5
import re
import sys

path = "/home/chenzewei/GraduationProject/corpus/";
name = "test_seg"
file = path+name+".txt"
if len(sys.argv) >= 2:
	file = argv[1]
	print("update the soruce file!")

f = open(file,'r')
line = f.readline()
d = dict()
count = 0 #difference word count
wdn = 0 #words_count
while line:
	l = re.split(r'[\s\,]+|[ ]+',line)
	for x in l:
		wdn += 1
		if x in d:
			d[x] += 1

		else:
			d[x]  = 1
			count  += 1
	line = f.readline()
	print("count = ",count)

print("Total words = ",wdn)
acnt = 0
for i in d:
	acnt += d[i]
print("all_plus = ",acnt)
print(d)
f.close()
