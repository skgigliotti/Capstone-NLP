import csv
import pandas as pd
from urllib import request
from textblob import TextBlob


origText = request.urlopen("https://www.olympic.org/news/ioc-ipc-tokyo-2020-organising-committee-and-tokyo-metropolitan-government-announce-new-dates-for-the-olympic-and-paralympic-games-tokyo-2020")

encoding = origText.info().get_content_charset()

if(encoding is None):
    encoding = "ISO-8859-1"


try:
    raw = origText.read().decode(encoding)

except Exception as e:
    print(e)


#convert texts to textBlobs
obj = TextBlob(raw)

pol = obj.sentiment.polarity

subj = obj.sentiment.subjectivity

print("pol: ")
print(pol)
print("subj: ")
print(subj)


newobj = obj.translate(to="fr")

newpol = newobj.sentiment.polarity

newsubj = newobj.sentiment.subjectivity

print("pol: ")
print(newpol)
print("subj: ")
print(newsubj)
