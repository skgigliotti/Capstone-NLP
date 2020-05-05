import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt
import seaborn as seabornInstance
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

#linear regression with guidance from https://towardsdatascience.com/a-beginners-guide-to-linear-regression-in-python-with-scikit-learn-83a8f7ae2b4f

dataset = pd.read_csv('output.csv')
#dataset.plot(x='polarity', y='subjectivity', style='o')

origPol = dataset['polarity'].iloc[0]
origSub = dataset['subjectivity'].iloc[0]

#calculate the deviation from the target polarity
for i in range (1,len(dataset)):
    lang = trPol = dataset['language'].iloc[i]

    trPol = dataset['polarity'].iloc[i]
    trSub = dataset['subjectivity'].iloc[i]

    devPol = abs(trPol - origPol)
    devSub = abs(trSub - origSub)

    line = [devPol,devSub,lang]

    with open('analyzeOutput.csv','a') as fd:
        writer = csv.writer(fd)
        writer.writerow(line)
