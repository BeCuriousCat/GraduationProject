rootdir=$PWD"/corpus/"
a=("zhonghe" "douhao" "gantanhao" "juhao" "wenhao" "maohao" "fenhao")

cd ./util

./getCorpus.py
echo ******${rootdir}${a[0]}

./getCorpus.py ${rootdir}${a[0]}
./getCorpus.py ${rootdir}${a[1]}
./getCorpus.py ${rootdir}${a[2]}
./getCorpus.py ${rootdir}${a[3]}
./getCorpus.py ${rootdir}${a[4]}
./getCorpus.py ${rootdir}${a[5]}
./getCorpus.py ${rootdir}${a[6]}


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
cd ../

