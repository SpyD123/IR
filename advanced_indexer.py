from math import log
s=raw_input()
s=s.lower()
s=s.split("---")

n=len(s)
words=[]
ind=[]
df=[]
tf=[]
tf_idf=[]

for i in range(len(s)):
        r=s[i].split(" ")
	r.remove('')
	se=set(r)
        for w in se:
		if w<>'':
			position=[]
			for x in range(len(r)):
				if r[x]==w:
					position.append(x)
			doc_pos=[i,position]
        		if w not in words:
				words.append(w)
				ind.append([])
			ind[words.index(w)].append(doc_pos)

#for wi in range(len(ind)):
#	print words[wi]," - > ",ind[wi]

for w in range(len(ind)):
	#print words[w]
	i=ind[w]
	d=len(i)
	#print d
	t=[]
	ti=[]
	for x in range(len(i)):
		y=i[x]
		#print y
		t.append([x,len(y[1])])	
		ft=0
		if len(y[1])==0:
			ft=0
		else:
			ft=log(len(y[1]),10)+1
		fdi=log(n/d,10)
		print words[w],y,len(y[1]),d
		print [words[w],y[0],ft,fdi,ft*fdi]
		tf_idf.append([words[w],y[0],ft,fdi,ft*fdi])
	tf.append([words[w],t]);
	df.append([words[w],d]);

for u in range(len(words)):
	print(words[u]),
	print(" ==> "),
	print(ind[u])
