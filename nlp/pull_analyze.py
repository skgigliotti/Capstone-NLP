import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.probability import FreqDist
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import subjectivity,stopwords
from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.util import *
import pandas as pd
from urllib import request


all_words = []
allowed_word_types = ["J"]

urlDivine = "http://www.gutenberg.org/files/8800/8800.txt"
#urlDivina = "http://www.gutenberg.org/files/1012/1012-0.txt"

responseE = request.urlopen(urlDivine)
#responseI = request.urlopen(urlDivina)

rawE = responseE.read().decode('utf8')
#rawI = responseI.read().decode('utf8')

stop_words_E=set(stopwords.words("english"))
#stop_wordsI=set(stopwords.words("italian"))

tokenized_word_E=word_tokenize(rawE)

#take out meaningless stop words such as the; this will be testing data
stoppedE = [w for w in tokenized_word_E if not w in stop_words_E]

#create training data
# parts of speech tagging for each word
pos = nltk.pos_tag(stoppedE)
neg = nltk.pos_tag(stoppedE)

# make a list of  all adjectives identified by the allowed word types list above
for w in pos:
    if w[1][0] in allowed_word_types:
        all_words.append(w[0].lower())

for w in neg:
        if w[1][0] in allowed_word_types:
            all_words.append(w[0].lower())

training_set = all_words[:1900]


# creating a frequency distribution of each adjectives.
all_words = nltk.FreqDist(all_words)

# listing the 5000 most frequent words
word_features = list(all_words.keys())[:5000]

# function to create a dictionary of features for each review in the list document.
# The keys are the words in word_features
# The values of each key are either true or false for wether that feature appears in the review or not

def find_features(document):
    words = word_tokenize(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)
    return features

# Creating features for each review
#featuresets = [(find_features(rev), category) for (rev, category) in documents]

# Shuffling the documents
#random.shuffle(featuresets)

training_set = [({'great': True, 'excellent': False, 'horrible': False}, 'pos')]
#testing_set = featuresets[20000:]

classifier = nltk.NaiveBayesClassifier.train(training_set)

print("Classifier accuracy percent:",(nltk.classify.accuracy(classifier, stoppedE))*100)

classifier.show_most_informative_features(15)

#sents = text.Sentiment.value_counts()

#print(sents)

#nltk.sentiment.util.save_file('today I feel good', output)
