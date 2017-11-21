from nltk import PorterStemmer
from nltk.tokenize import TweetTokenizer
from collections import OrderedDict
from collections import Counter
import collections
import os
tkn = TweetTokenizer()
punct = ',...?!'
words_dict = {}
words_dict_te = {}
path = '/home/ayushi/IR-Assignment1/Assignment/DataCorpus'
with open("data.txt", "w") as pt:
  for itemName in os.listdir(path):
    itemName = os.path.join(path, itemName)
    if os.path.isfile(itemName):
        s= file(itemName, 'r').read()
	wl = tkn.tokenize(s)
	for x in wl:
	 x=x.lower()
	 if (x).strip() and (x).strip() not in punct:
                words_dict[x] = words_dict.get((x),0) + 1
words_dict = OrderedDict(sorted(words_dict.items(), key=lambda t: t[1], reverse=True))
counts = Counter(words_dict)
c = collections.Counter(words_dict)

for letter in words_dict:
	print(letter, c[letter])    
