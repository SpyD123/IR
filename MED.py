s1=raw_input("Word 1 :")
s2=raw_input("Word 2 :")
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
	print dis[i]
print "Minimum Edit Distance = ",dis[len(s1)][len(s2)]
