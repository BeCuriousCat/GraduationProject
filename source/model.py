#!/usr/bin/python3.5

from keras.preprocessing import text

t = open("/home/chenzewei/GraduationProject/corpus/The_three_body_replace_y.txt").readlines()

X_train = open("/home/chenzewei/GraduationProject/corpus/The_three_body__replace_x.txt").readlines()
print(len(t)," ",len(X_train))