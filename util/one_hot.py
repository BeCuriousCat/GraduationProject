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

