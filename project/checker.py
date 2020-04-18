import csv
import pandas as pd
from urllib import request
from textblob import TextBlob
from nltk.corpus import subjectivity,stopwords
from nltk.tokenize import sent_tokenize, word_tokenize

POL = [0.00156300045897086,0.116686091686091]
SUBJ = [0.00720380833741163,0.0680546977931489]

def check(inputText):
  objEn = TextBlob(inputText[0])
  objFr = TextBlob(inputText[1])

  pol = abs(objEn.sentiment.polarity - objFr.sentiment.polarity)

  subj = abs(objEn.sentiment.subjectivity - objFr.sentiment.subjectivity)

  polcheck = False
  subjcheck = False

  if (pol >= POL[0]) and (pol <= POL[1]):
      polcheck = True

  if (subj >= SUBJ[0]) and (subj <= SUBJ[1]):
      subjcheck = True
  print(subj)
  print(pol)
  return polcheck and subjcheck



inputURLs = ["https://www.who.int/news-room/detail/30-03-2020-who-releases-guidelines-to-help-countries-maintain-essential-health-services-during-the-covid-19-pandemic","https://www.who.int/fr/news-room/detail/30-03-2020-who-releases-guidelines-to-help-countries-maintain-essential-health-services-during-the-covid-19-pandemic"]
#get the texts from project Gutenberg
response1 = request.urlopen(inputURLs[0])
response2 = request.urlopen(inputURLs[1])

#get the encoding to decode to text
encoding1 = response1.info().get_content_charset()
encoding2 = response2.info().get_content_charset()

if(encoding1 is None):
    encoding1 = "ISO-8859-1"
if(encoding2 is None):
    encoding2 = "ISO-8859-1"


try:
    raw1 = response1.read().decode(encoding1)
    raw2 = response1.read().decode(encoding2)

except Exception as e:
    print(e)

print(check([raw1,raw2]))
