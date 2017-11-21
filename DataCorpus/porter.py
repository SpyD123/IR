from nltk import PorterStemmer   
import urllib
from bs4 import BeautifulSoup

f=open('list', 'r')
st=f.read()
f.close()
st=st.split("\n")

for ur in st:
	if ur[0:1]=="e":
		url = ur
		html = urllib.urlopen(url).read()
		soup = BeautifulSoup(html,"lxml")

		for script in soup(["script", "style"]):
	    		script.extract()

		text = soup.get_text()  
		s=text
		s=s.lower()
		s=s.split(" ")
		s=s[1:]
		for i in s:
			i=i.split("\n")
			i=i[0]
			print(PorterStemmer().stem_word(i)),
		print("---"),
