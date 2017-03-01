rootdir="/home/chenzewei/GraduationProject/corpus/"

a=("test" "test2" "test3" "test4" "test5" "test6" "test7" "test8")

cd ./util

./getCorpus.py

./getCorpus.py ${rootdir}${a[0]}
./getCorpus.py ${rootdir}${a[1]}
./getCorpus.py ${rootdir}${a[2]}
./getCorpus.py ${rootdir}${a[3]}
./getCorpus.py ${rootdir}${a[4]}
./getCorpus.py ${rootdir}${a[5]}
./getCorpus.py ${rootdir}${a[6]}
./getCorpus.py ${rootdir}${a[7]}

cd ../

cd ./source
./segmentation.py classes ../tmp/
./segmentation.py ${a[0]} ../tmp/
./segmentation.py ${a[1]} ../tmp/
./segmentation.py ${a[2]} ../tmp/
./segmentation.py ${a[3]} ../tmp/
./segmentation.py ${a[4]} ../tmp/
./segmentation.py ${a[5]} ../tmp/
./segmentation.py ${a[6]} ../tmp/
./segmentation.py ${a[7]} ../tmp/
cd ../