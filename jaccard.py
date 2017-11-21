import math
txt = open("test")
st=txt.read()
s=raw_input("Enter the query :")
st=st.split("\n")
data=[]
for x in st:
	data=data+x.split()
query=s.split()
data=set(data)
query=set(query)
inter=data.intersection(query)
uni=data.union(query)
#print inter
#print uni
#print data
#print query
print "Jaccard = ",(float)(len(inter))/(float)(len(uni))
