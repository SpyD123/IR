from nltk import PorterStemmer

s=raw_input('')
s=s.lower()
s=s.split(" ")

for i in s:
	print(PorterStemmer().stem_word(i)),

print("---"),
