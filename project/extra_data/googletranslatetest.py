from googletrans import Translator
import csv
import pandas as pd
import requests
from urllib import request
from textblob import TextBlob
from nltk.corpus import subjectivity,stopwords
from nltk.tokenize import sent_tokenize, word_tokenize

translator = Translator()

origText = request.urlopen("http://www.gutenberg.org/files/2000/2000-8.txt")

encoding = origText.info().get_content_charset()

if(encoding is None):
    encoding = "ISO-8859-1"


try:
    raw = origText.read().decode(encoding)

except Exception as e:
    print(e)


#convert texts to textBlobs
obj = TextBlob(raw)

#get the lengths of the texts
len1 = len(raw)

direct = translator.translate("Most people start\n at our Web site which has the main PG search facility: \n http://www.gutenberg.net Éstos, creyendo que la pesadumbre de verse vencido y de no ver cumplido su deseo en la libertad y desencanto",src="es");
print(len1)
print(direct)
