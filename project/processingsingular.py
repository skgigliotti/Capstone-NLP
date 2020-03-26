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

    #get the encoding to decode to text
    encoding = response.info().get_content_charset()

    if(encoding is None):
        encoding = "ISO-8859-1"


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

    line = [url,lang,len1,pol,subj]

    #write information in csv
    with open('output.csv','a') as fd:
        writer = csv.writer(fd)
        writer.writerow(line)


with open('input.csv') as csvfile:
    input = csv.reader(csvfile, delimiter=',')
    #go through each row in the input file and
    for i,row in enumerate(input):
        pullTexts([row[0],row[1]])
