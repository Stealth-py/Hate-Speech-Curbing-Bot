from nltk.classify import NaiveBayesClassifier
from nltk.corpus import subjectivity
from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.util import *
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import tokenize
import pandas as pd
from funny_words import build_n_gram
df = pd.read_excel('expandedLexicon.xlsx')
df_words = df['Word_type']
ls_onlywords = []
for i in df_words:
    ls_words.append(i)
for i in range(len(ls_words)):
    ls_onlywords.append(ls_words[i].split("_")[0])
def sentivader(message):
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
                sentences[m] = ' '.join(ls_sentence)
        print(sentences)
        print(sentiment)
        print(ss)
    return ' '.join(sentences)
print(sentivader(input()))