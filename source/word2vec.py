import gensim.models.word2vec as w2v
#model_file_name = 'language.txt'
sentences = w2v.LineSentence('/corpus/The_three_body.txt')
model = w2v.Word2Vec(sentences,size=20,window=5,min_count=5,workers=4)
model.save('/corpus/dc.txt')
