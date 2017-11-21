from math import log
s=raw_input()
s=s.lower()
s=s.split("---")


r=[]
for s1 in s:
	r+=s1.split(" ")

se=set(r)
V=len(se)
N=len(r)
K=7.34
print("Beta ="),
print(log((V/K),N))
