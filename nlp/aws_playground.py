import boto3
import json
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
        try:
            raw2 = response2.read().decode('ISO-8859-1')
        except:
            print(e)

    return [raw1,lang1, raw2, lang2]

texts = pullTexts(["https://www.poetrytranslation.org/poems/the-women-who-really-drove-me-crazy/original", "sp", "https://www.poetrytranslation.org/poems/the-women-who-really-drove-me-crazy", "en"])
comprehend = boto3.client(service_name='comprehend')

text = "It is raining today in Seattle"

print('Calling DetectSentiment')
print(json.dumps(comprehend.detect_sentiment(Text=texts[2], LanguageCode=texts[3]), sort_keys=True, indent=4))
print(json.dumps(comprehend.detect_sentiment(Text=texts[1], LanguageCode=texts[2]), sort_keys=True, indent=4))
print('End of DetectSentiment\n')
