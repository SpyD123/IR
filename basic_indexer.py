s=raw_input()
s=s.lower()
s=s.split("---")

words=[]
ind=[]
zeroes=[0]*len(s)

for i in range(len(s)):
	r=s[i].split(" ")
	for x in r:
		zeroes=[0]*len(s)
		if x<>'':
			if x not in words:
				words.append(x)
				ind.append(zeroes)
			'''print(x,words.index(x),i,ind[words.index(x)][i])'''
			ind[words.index(x)][i]=1
for w in range(len(words)):
	print(ind[w])
	print(words[w])
