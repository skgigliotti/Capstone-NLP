import nltk
import csv
import pandas as pd
from urllib import request
from textblob import TextBlob
from nltk.corpus import subjectivity,stopwords
from nltk.tokenize import sent_tokenize, word_tokenize


def pullTexts(textVec):
    url = textVec[0]

    lang = textVec[1]

    #get the texts from project Gutenberg
    response = request.urlopen(url)

    encoding = response.info().get_content_charset()

    if(encoding is None):
        encoding = "ISO-8859-1"

    print(encoding)

    try:
        raw = response.read().decode(encoding)

    except Exception as e:
        print(e)


    #convert texts to textBlobs
    obj = TextBlob(raw)

    #get the lengths of the texts
    len1 = len(raw)

    #Use textBlob to calculate polarity and subjectivity of texts
    pol = obj.sentiment.polarity

    subj = obj.sentiment.subjectivity

    #write information in csv
    line = (url + "," + lang + "," + str(len1) + "," + str(pol)+ "," + str(subj)+ "," + "\n")

    with open('bibleoutput.csv','a') as fd:
        fd.write(line)

with open('bibleinput.csv') as csvfile:
    input = csv.reader(csvfile, delimiter=',')
    for row in input:
        pullTexts([row[0],row[1]])
