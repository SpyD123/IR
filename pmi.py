import math
txt = open("test")
st=txt.read()
s=raw_input("Enter the query :")
st=st.split("\n")
data=[]
for x in st:
	data=data+x.split()
#print data
total=0.0
query=s.split()
for x in range(1,len(data)):
	if query[0]==data[x-1] and query[1]==data[x]:
		total=total+1.0
#print total
total=(2*total)/(len(data)*(len(data)-1))
prod=1.0
for term in query:
	#print term
	prod=prod*data.count(term)
	#print data.count(term)
	prod=prod/len(data)
#print prod
#print total/prod
print "PMI = ",math.log(total/prod)
