import nltk
import pandas as pd
from urllib import request
from textblob import TextBlob
from nltk.corpus import subjectivity,stopwords
from nltk.tokenize import RegexpTokenizer
from nltk.tokenize import sent_tokenize, word_tokenize


urlDivine = "http://www.gutenberg.org/files/8800/8800.txt"
urlDivina = "http://www.gutenberg.org/files/1012/1012-0.txt"

responseE = request.urlopen(urlDivine)
responseI = request.urlopen(urlDivina)

rawE = responseE.read().decode('utf8')
rawI = responseI.read().decode('utf8')

stop_words_E=set(stopwords.words("english"))
#stop_wordsI=set(stopwords.words("italian"))

tokenizer = RegexpTokenizer(r'\w+')

tokenized_word_E=tokenizer.tokenize(rawE)

obj1 = TextBlob(rawE)

print(obj1.noun_phrases[0:50])

#take out meaningless stop words such as the; this will be testing data
stoppedE = [w for w in tokenized_word_E if not w in stop_words_E]

frequency_dist = nltk.FreqDist(stoppedE)
print(sorted(frequency_dist,key=frequency_dist.__getitem__, reverse=True)[0:50])
