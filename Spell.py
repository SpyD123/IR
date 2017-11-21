s1=raw_input("Word 1 :")
f = open("unigram.txt",'r')
unigrams = f.read()
f.close()
m=len(s1)
#mword=unigram[0]
unigram=unigrams.split()
mword=unigram[0]
for u in range(len(unigram)):
	s2=unigram[u]
	dis = [[0 for x in range(len(s2)+1)] for y in range(len(s1)+1)] 
	#print dis
	for i in range(len(s1)+1):
		dis[i][0]=i
	for j in range(len(s2)+1):
	        dis[0][j]=j
	#print dis
	for i in range(1,len(s1)+1):
		for j in range(1,len(s2)+1):
			a=2
			if s2[j-1]==s1[i-1]:
				a=0
			#print s2[j-1]," ",s1[i-1]," ",
			#print a
			dis[i][j]=min(dis[i-1][j]+1,dis[i][j-1]+1,dis[i-1][j-1]+a)
		#print dis[i]
	if m>dis[len(s1)][len(s2)]:
		mword=s2
		m=dis[len(s1)][len(s2)]
print mword
