from nltk.classify import NaiveBayesClassifier
from nltk.corpus import subjectivity
from nltk.downloader import update
from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.util import *
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import tokenize
import pandas as pd
from funny_words import build_n_gram

sid = SentimentIntensityAnalyzer()
df = pd.read_excel('abuse_dir\expandedLexicon.xlsx')
df_words = df['Word_type']
ls_words = []
ls_onlywords = []
ls_words = []
for i in df_words:
    ls_words.append(i)
for i in range(len(ls_words)):
    ls_onlywords.append(ls_words[i].split("_")[0])

def sentivader(message):
    f = False
    sentences = list(message.split('.'))
    ls_sentiment = []
    for i in range(len(sentences)):
        ss = sid.polarity_scores(sentences[i])
        sentiment = 0
        for k in sorted(ss):
            if k == 'compound':
                sentiment = sentiment + ss[k]
                ls_sentiment.append(ss[k])
    for m in range(len(sentences)):
        if ls_sentiment[m] > 0:
            pass
        else:
            ls_sentence = sentences[m].split()
            for j in range(len(ls_sentence)):
                if ls_sentence[j] in ls_onlywords:
                    ls_sentence[j] = build_n_gram()
                    f = True
                sentences[m] = ' '.join(ls_sentence)
        # print(sentences)
        # print(sentiment)
        # print(ss)
        updated_message = ' '.join(sentences)
    return (f, updated_message)
# print(sentivader(input()))
