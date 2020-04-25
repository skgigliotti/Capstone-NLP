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
    txt = textVec[0]

    lang = textVec[1]

    file = 'data/' + lang + '/' + txt

    raw = open(file,'r').read()


    #convert texts to textBlobs
    obj = TextBlob(raw)

    #get the lengths of the texts
    len1 = len(raw)

    #Use textBlob to calculate polarity and subjectivity of texts
    pol = obj.sentiment.polarity

    subj = obj.sentiment.subjectivity

    posTags = obj.pos_tags

    counts = posCounts(posTags)

    if lang == 'en':
        translatedObj = translateText(obj,'fr')

        translatedPosTags = translatedObj.pos_tags

        tCounts = posCounts(translatedPosTags)

        tPol = translatedObj.sentiment.polarity

        tSubj = translatedObj.sentiment.subjectivity

    else:
        tCounts = [0,0,0]
        tPol = 0
        tSubj = 0

    line = [txt,lang,len1,pol,subj,counts[0],counts[1],counts[2],tPol,tSubj,tCounts[0],tCounts[1],tCounts[2]]

    return line

def writeData(line1,line2):
    line2 = line2[0:8]

    #difference between English and French polarity and subjectivity
    polDiff = [abs(line1[3] - line2[3])]
    subjDiff = [abs(line1[4] - line2[4])]

    #difference between number of adjectives,adverbs,and verbs in the English and French versions
    posDiff = [abs(line1[5] - line2[5]),abs(line1[6] - line2[6]),abs(line1[7] - line2[7])]

    #difference between original and autotranslated polarity and subjectivity
    tPolDiff = [abs(line1[3] - line1[8])]
    tSubjDiff = [abs(line1[4] - line1[9])]

    #difference between number of adjectives,adverbs,and verbs in the original and translated versions
    tPosDiff = [abs(line1[5] - line1[10]),abs(line1[6] - line1[11]),abs(line1[7] - line1[12])]

    #write information in csv
    lineCombined = line1 + line2 + polDiff + subjDiff + posDiff + tPolDiff + tSubjDiff + tPosDiff

    with open('enfroutput.csv','a') as fd:
        writer = csv.writer(fd)
        writer.writerow(lineCombined)

with open('enfrdata.csv') as csvfile:
    input = csv.reader(csvfile, delimiter=',')
    #go through each row in the input file and
    for i,row in enumerate(input):
        line1 = pullTexts([row[0],row[1]])
        line2 = pullTexts([row[2],row[3]])
        writeData(line1,line2)
