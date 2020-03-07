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

    raw1 = None
    raw2 = None

    try:
        raw1 = response1.read().decode('utf8')

    except Exception as e:
        print(e)

    if raw1 is None:
        raw1 = response1.read().decode('ISO-8859-1')


    try:
        raw2 = response2.read().decode('utf8')

    except Exception as e:
        print(e)

    if raw2 is None:
        print("oye")
        try:
            raw2 = response2.read().decode('ISO-8859-1')
        except:
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

    #write information in csv
    line = (url1 + "," + lang1 + "," + str(len1) + "," + str(pol1)+ "," + str(subj1)+ "," + url2 + "," + lang2 + "," + str(len2) + "," + str(pol2) + "," + str(subj2) + "\n")

    with open('data.csv','a') as fd:
        fd.write(line)

pullTexts(["http://www.gutenberg.org/cache/epub/17489/pg17489.txt", "french", "http://www.gutenberg.org/cache/epub/135/pg135.txt", "english"])
