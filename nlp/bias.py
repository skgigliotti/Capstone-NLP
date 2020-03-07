import nltk
import csv
import pandas as pd
from urllib import request
from textblob import TextBlob
from nltk.corpus import subjectivity,stopwords
from nltk.tokenize import sent_tokenize, word_tokenize


def findBias(textVec):

    #convert texts to textBlobs
    obj1 = TextBlob(textVec[1])

    #Use textBlob to calculate polarity and subjectivity of texts
    pol1 = obj1.sentiment.polarity

    subj1 = obj1.sentiment.subjectivity

    title = textVec[0]
    #write information in csv
    line = (title + "," + str(pol1)+ "," + str(subj1) + "\n")

    with open('bias_data.csv','a') as fd:
        fd.write(line)

findBias(["Poster Policy","Dear Students, Throughout the day I have heard from several of you about your response to my email sent earlier today and I am writing to apologize. I have learned that my words and the tone in the email contributed to silencing students, particularly students of color. I am so sorry for how I have added to frustration, anger and hurt in the conversations and engagement around race, ethnicity and diversity. I was motivated by care for all our students - those who posted and those who defaced the posters - but I failed to recognize how my email would be silencing. I offer my sincere apology. There are events and initiatives that will occur after spring break to address race and diversity. These are intended to more widely open the conversation on our campus. Look for an email from the Executive Team tomorrow that will include comments about these plans among other things. I trust you will receive this email in the spirit in which it is intended - with humility, deep care for all our students and hope that we can move forward together. I am committed to continuing to pursue better conversations and make changes so we can be a stronger community for everyone. I also recommit to my personal journey of understanding and growth. With God’s help, I know we, and I, can make progress.Blessings, Edee"])
