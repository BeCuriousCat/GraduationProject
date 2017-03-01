#!/bin/bash
cd ./util
./getCorpus.py
./getCorpus.py /home/chenzewei/GraduationProject/corpus/test 
cd ../
pwd
cd ./source
./segmentation.py classes ../tmp/

./segmentation.py test ../tmp/
cd ../

