import csv
import pandas as pd
from urllib import request
from textblob import TextBlob
from nltk.corpus import subjectivity,stopwords
from nltk.tokenize import sent_tokenize, word_tokenize

bigramdict = {}

def pullTexts(textVec):
    url = textVec[0]

    #get the texts from project Gutenberg
    response = request.urlopen(url)

    #get the encoding to decode to text
    encoding = response.info().get_content_charset()

    if(encoding is None):
        encoding = "ISO-8859-1"


    try:
        raw = response.read().decode(encoding)
        return raw

    except Exception as e:
        print(e)

def createDictionary(text):
    #split on words
    words = text.split()

    #initialize previous 2 words for bigram model
    prev0 = words[0].lower()
    #prev1 = words[1].lower()

    #go through all the words and put the frequencies in a ditionary
    for w in words[1:]:

        bigram = prev0 + ' ' + w.lower()

        if bigram in bigramdict.keys():
            bigramdict[bigram] = bigramdict[bigram] + 1
        else:
            bigramdict[bigram] = 1

        #prev1 = prev0
        #update previous value
        prev0 = w.lower()



with open('enfrinput.csv') as csvfile:
    input = csv.reader(csvfile, delimiter=',')
    #go through each row in the input file and
    #for i,row in enumerate(input):
        #text = pullTexts([row[2],row[3]])
    text = open('frolympics.txt','r').read()
    createDictionary(text)

    print(bigramdict)
