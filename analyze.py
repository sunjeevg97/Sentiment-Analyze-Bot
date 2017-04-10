import praw
import requests
import requests.auth
import oauth
from bs4 import BeautifulSoup
import csv
import re, math, collections, itertools
import nltk, nltk.classify.util, nltk.metrics
from nltk.classify import NaiveBayesClassifier
from nltk.metrics import BigramAssocMeasures
from nltk.probability import FreqDist, ConditionalFreqDist
import pandas as pd

df = pd.read_csv('dataset.csv', error_bad_lines = False)

positive_sentences = df.loc[df['Sentiment'] == 1]
negative_sentences = df.loc[df['Sentiment'] == 0]

print negative_sentences
'''comments = open('comments.csv')
csv_f = csv.reader(comments)

with csv_f as f:
    data = f.read().split().("\n")

random.shuffle(data)

train_data = data[:60]
test_data = data[40:]

for rows in train_data:
    word_tokenize(rows)'''
