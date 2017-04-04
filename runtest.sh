rootdir="/home/chenzewei/GraduationProject/corpus/"

a=("test" "test2" "test3" "test4" "test5")

cd ./util

./getCorpus.py

./getCorpus.py ${rootdir}${a[0]}
./getCorpus.py ${rootdir}${a[1]}
./getCorpus.py ${rootdir}${a[2]}
./getCorpus.py ${rootdir}${a[3]}
./getCorpus.py ${rootdir}${a[4]}


cd ../

cd ./source
./segmentation.py classes ../tmp/
./segmentation.py ${a[0]} ../tmp/
./segmentation.py ${a[1]} ../tmp/
./segmentation.py ${a[2]} ../tmp/
./segmentation.py ${a[3]} ../tmp/
./segmentation.py ${a[4]} ../tmp/
cd ../