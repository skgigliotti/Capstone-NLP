import csv
import pandas as pd
from urllib import request
from textblob import TextBlob
from nltk.corpus import subjectivity,stopwords
from nltk.tokenize import sent_tokenize, word_tokenize

frquenciesdict = {}
transitionsdict = {}

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

def createDictionary(texts,n):
    #split on words
    words = []

    for t,text in enumerate(texts):
        str = texts[text]
        clean = str.lower().strip(",").replace("."," .").replace("!", " !").replace("?", " ?").replace("¿", "¿ ").split()
        words = words + clean
    ngramdict = {}
    #go through all the words and put the frequencies in a ditionary
    for i in range(len(words)-n+1):

        ngram = words[i:i+n]
        ngram = ' '.join(ngram)

        if ngram in ngramdict.keys():
            ngramdict[ngram] = ngramdict[ngram] + 1
        else:
            ngramdict[ngram] = 1

    return ngramdict

def calcProb(text,trans,overall):
    words = text.lower().strip(",").replace("."," .").replace("!", " !").replace("?", " ?").replace("¿", "¿ ").split()
    strwords = ' '.join(words)
    substr = ' '.join(words[:len(words)-1])
    if strwords in trans:
        num = trans[strwords]

        denom = overall[substr]

        return num/denom

    elif substr in overall:
        return 0.01/overall[substr]
    else:
        return 0


def train(input_text):
    print(input_text)
    files = {}
    with open('userinterface/markov/enfrdata.csv') as csvfile:
        input = csv.reader(csvfile, delimiter=',')

        #go through each row in the input file and
        for i,row in enumerate(input):
            location = 'userinterface/markov/data/fr/'+row[2]
            files[row[2]] = open(location,'r').read()
    #text = open('frolympics.txt','r').read()
    #blob = TextBlob(text)

    #return 1
    #text1 = input('Please enter your first option')
    #text2 = input('Please enter your second option')

    frquenciesdict = createDictionary(files,len(input_text[0].split())-1)
    transitionsdict = createDictionary(files,len(input_text[0].split()))

    #return a comparison of the 2 options
    return [calcProb(input_text[0],transitionsdict,frquenciesdict),calcProb(input_text[1],transitionsdict,frquenciesdict)]
