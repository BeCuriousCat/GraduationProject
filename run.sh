#!/bin/bash

#运行java,预处理预料
cd ./bin
java Main
java Main test
cd ../

#将预处理结果进行分词

cd source/
./segmentation.py The_three_body
./segmentation.py test
cd ../

#运行神经网络
cd source/
./neuralNetwork.py
cd ../