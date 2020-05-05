import nltk
import csv
import pandas as pd
from urllib import request
from textblob import TextBlob
from nltk.corpus import subjectivity,stopwords
from nltk.tokenize import sent_tokenize, word_tokenize


def pullTexts(textVec):
    url1 = textVec[0]
    url2 = textVec[2]

    lang1 = textVec[1]
    lang2 = textVec[3]

    #get the texts from project Gutenberg
    response1 = request.urlopen(url1)
    response2 = request.urlopen(url2)

    #get the encoding
    encoding1 = response1.info().get_content_charset()
    encoding2 = response2.info().get_content_charset()

    if(encoding1 is None):
        encoding1 = "ISO-8859-1"
    if (encoding2 is None):
        encoding2 = "ISO-8859-1"
        
    try:
        raw1 = response1.read().decode(encoding1)

    except Exception as e:
        print(e)


    try:
        raw2 = response2.read().decode(encoding2)

    except Exception as e:
        print(e)

    #convert texts to textBlobs
    obj1 = TextBlob(raw1)
    obj2 = TextBlob(raw2)

    #get the lengths of the texts
    len1 = len(raw1)
    len2 = len(raw2)

    #Use textBlob to calculate polarity and subjectivity of texts
    pol1 = obj1.sentiment.polarity
    pol2 = obj2.sentiment.polarity

    subj1 = obj1.sentiment.subjectivity
    subj2 = obj2.sentiment.subjectivity

    diffP = abs(pol1 - pol2)
    diffS = abs(subj1 - subj2)

    #write information in csv
    line = (url1 + "," + lang1 + "," + str(len1) + "," + str(pol1)+ "," + str(subj1)+ "," + url2 + "," + lang2 + "," + str(len2) + "," + str(pol2) + "," + str(subj2) + "," + str(diffP) + "," + str(diffS) + "\n")

    with open('output.csv','a') as fd:
        fd.write(line)

with open('input.csv') as csvfile:
    input = csv.reader(csvfile, delimiter=',')
    for row in input:
        pullTexts([row[0],row[1],row[2],row[3]])
