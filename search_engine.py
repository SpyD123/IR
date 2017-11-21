import math
from nltk import PorterStemmer 
f=open("input","r+")
s=f.read()
f.close()
s=s.lower()
s=s.split("---")

n=len(s)
words=[]
ind=[]
df=[]
tf=[]
tf_idf=[]
net=[0]*n
net_c=[]
net_j=[]
net_f=[]

for i in range(len(s)):
        r=s[i].split(" ")
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

query=raw_input("Enter Query : ")
q=query.split()
query=""

for x in range(len(q)):
	q[x]=q[x].lower()
	q[x]=PorterStemmer().stem_word(q[x])
	query=query+q[x]+" "

for w in range(len(ind)):
	i=ind[w]
	d=len(i)
	t=[]
	ti=[]
	for x in range(len(i)):
		y=i[x]
		t.append([x,len(y[1])])	
		ft=0
		if len(y[1])==0:
			ft=0
		else:
			ft=math.log(len(y[1]),10)+1
		fdi=math.log(n/d,10)
		tf_idf.append([words[w],y[0],ft,fdi,ft*fdi])#word, docnum ,tf ,idf , product
		if words[w] in q:
			net[y[0]]=net[y[0]]+ft*fdi
	tf.append([words[w],t])
	df.append([words[w],d])

selected=[]
found=0
if max(net)==0:
	print "No Result Found !"
	found=1

if found<>1:
	for i in range(0,10):
		selected.append(net.index(max(net)))
		net[net.index(max(net))]=0

	#print selected
	q2=query.split()
	q1=set(q2)

	for select in selected:
		st=s[select]
		st=st.split("\n")
		data=[]
		for x in st:
		        data=data+x.split()
		data1=set(data)
		total=0.0
		v1=[]
		v2=[]
		terms=[]
		net1=0
		net2=0
		inter=data1.intersection(q1)
		uni=data1.union(q1)
		for term in q2:
		        if not(term in terms):
		                v1.append((float)(data.count(term)))
		                net1=net1+(float)(data.count(term))
		                v2.append((float)(q2.count(term)))
		                net2=net2+(float)(q2.count(term))
		                terms.append(term)
		for x in range(len(v1)):
		        if net1<>0:
				v1[x]=v1[x]/net1
			else:
				v1[x]=0
			if net2<>0:
		        	v2[x]=v2[x]/net2
			else:
				v2[x]=0
		a=0.0
		b=0.0
		c=0.0
		for x in range(len(v1)):
		        a=a+v1[x]*v2[x]
		        b=b+v1[x]*v1[x]
		        c=c+v2[x]*v2[x]
		b=math.sqrt(b)
		c=math.sqrt(c)
		if b<>0 and c<>0:
			cosi=a/(b*c)
		else :
			cosi=0
		net_c.append(math.acos(cosi))
		net_j.append((float)(len(inter))/(float)(len(uni)))
		net_f.append(net_j[-1]-net_c[-1])

	#print net_c
	#print net_j
	#print net_f
	ranking=[]

	for i in range(0,10):
		ranking.append(selected[net_f.index(max(net_f))])
		net_f[net_f.index(max(net_f))]=-100000

	#print ranking
	f=open("list","r+")
	order=f.read()
	f.close()
	order=order.split("\n")
	
	for r in range(len(ranking)):
		rank=ranking[r]
		print "Rank ",r," Document is :",
		print order[rank]

