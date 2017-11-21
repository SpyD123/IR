from nltk import PorterStemmer
from math import log
import math
#!/usr/bin/env python
from nltk.tokenize import TweetTokenizer
from collections import OrderedDict
from collections import Counter
import collections
import os
tkn = TweetTokenizer()
punct = ',...?!$0123456789<title><docno><doc></title><text>"()</doc>-5.315.3025180w</text>'
words_dict = {}
words_dict_en = {}
words_dict_te = {}
n=0
x1="a"
x2="a"
x3="a"
x11="a"
x22 = "a"
path = '/home/chaitanya/Assignment/DataCorpus'
#path = '/home/harshitha/Downloads/Assignment/DataCorpus'
with open("data.txt", "w") as pt:
  for itemName in os.listdir(path):
    #Loops over each itemName in the path. Joins the path and the itemName
    #and assigns the value to itemName.
    itemName = os.path.join(path, itemName)

    if os.path.isfile(itemName):
        s= file(itemName, 'r').read()
#s=raw_input('')
	wl = tkn.tokenize(s)
        #print wl
	n=n+ len(wl)
	for x in wl:
	 x=x.lower()
	 #if (x).strip() and (x).strip() not in punct:
                #words_dict[x] = words_dict.get((x),0) + 1
#words_dict = OrderedDict(sorted(words_dict.items(), key=lambda t: t[1], reverse=True))
#counts = Counter(words_dict)
	 x3=x2
	 x2=x1
	 x1=x
	 #if(x =='en' or x =='te' or x =='univ'):
	
         if (x3).strip() and (x3).strip() not in punct and len(x3)>2:
		
                words_dict_en[x3+' '+x11] = words_dict_en.get((x3),0) + 1
		words_dict[x] = words_dict.get((x),0) + 1
		x11=x3
	 #if(x == "te"):
	  #  if (x3).strip() and (x3).strip() not in punct and len(x3)>2:
	#	words_dict_te[x22+x3] = words_dict_te.get((x3),0) + 1
	#	x22=x3
words_dict = OrderedDict(sorted(words_dict.items(), key=lambda t: t[1], reverse=True))
words_dict_en = OrderedDict(sorted(words_dict_en.items(), key=lambda t: t[1], reverse=True))
#words_dict_te = OrderedDict(sorted(words_dict_te.items(), key=lambda t: t[1], reverse=True))
count = 0
count1 = 0
topwrds_list_en = []
topwrds_list_te = []
enl = len(words_dict_en)
tel = len(words_dict)
print enl
print tel
t=enl/5
y=tel/5
print t
print y

for x in words_dict_en:
    if (count<=t):
        topwrds_list_en.append(x)
        count = count + 1
    else:
        break
for x in words_dict:
    if (count1<=y):
        topwrds_list_te.append(x)
        count1 = count1 + 1
    else:
        break
with open("bigram.txt", "w") as xt:
    for x in topwrds_list_en:
        xt.write(x+"\n")
with open("unigram.txt", "w") as xt:
    for x in topwrds_list_te:
        if( x  not in punct and x != "'"):
        	xt.write(x+"\n")

