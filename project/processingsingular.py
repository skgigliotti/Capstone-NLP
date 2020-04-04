import csv
import pandas as pd
from urllib import request
from textblob import TextBlob
from nltk.corpus import subjectivity,stopwords
from nltk.tokenize import sent_tokenize, word_tokenize

VERBS = ["VBZ","VBP","VBN","VBG","VBD","VB"]
ADV = ["RB","RBR","RBS","WRB"]
ADJ = ["JJ","JJR","JJS"]
def translateText(blob,targetLang):
    newBlob = blob.translate(to=targetLang)

    return newBlob

def posCounts(posTags):
    #prepare to count adj, adv, and verbs
    adjCount = 0
    advCount = 0
    verbCount = 0
    #helpful video for pos tagging https://www.youtube.com/watch?v=aWhqoPLr6Jg
    for word,pos in posTags:
        if pos in ADJ:
            adjCount += 1

        if pos in ADV:
            advCount += 1

        if pos in VERBS:
            verbCount += 1
    return [adjCount,advCount,verbCount]

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

    posTags = obj.pos_tags


    counts = posCounts(posTags)

    translatedObj = translateText(obj,"ru")

    translatedPosTags = translatedObj.pos_tags

    tCounts = posCounts(translatedPosTags)

    tPol = translatedObj.sentiment.polarity

    tSubj = translatedObj.sentiment.subjectivity


    line = [url,lang,len1,pol,subj,counts[0],counts[1],counts[2],tPol,tSubj,tCounts[0],tCounts[1],tCounts[2]]

    #write information in csv
    with open('olympicsoutput.csv','a') as fd:
        writer = csv.writer(fd)
        writer.writerow(line)


with open('olympicsinput.csv') as csvfile:
    input = csv.reader(csvfile, delimiter=',')
    #go through each row in the input file and
    for i,row in enumerate(input):
        pullTexts([row[0],row[1]])
