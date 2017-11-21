import math
txt = open("test")
st=txt.read()
s=raw_input("Enter the query :")
st=st.split("\n")
data=[]
for x in st:
	data=data+x.split()
total=0.0
query=s.split()
v1=[]
v2=[]
terms=[]
net1=0
net2=0
for term in query:	
	if not(term in terms):
		v1.append((float)(data.count(term)))
		net1=net1+(float)(data.count(term))
		v2.append((float)(query.count(term)))
		net2=net2+(float)(query.count(term))
		terms.append(term)
#print v1
#print v2
for x in range(len(v1)):
	v1[x]=v1[x]/net1
	v2[x]=v2[x]/net2
#print v1
#print v2
a=0.0
b=0.0
c=0.0
for x in range(len(v1)):
	a=a+v1[x]*v2[x]
	b=b+v1[x]*v1[x]
	c=c+v2[x]*v2[x]
	#print b
	#print c
b=math.sqrt(b)
c=math.sqrt(c)
#print a
#print c
cosi=a/(b*c)
print math.acos(cosi)
