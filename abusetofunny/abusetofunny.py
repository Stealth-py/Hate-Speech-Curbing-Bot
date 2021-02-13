import pandas as pd
from funny_words import build_n_gram
df = pd.read_excel('expandedLexicon.xlsx')
df_words = df['Word_type']
ls_onlywords = []
ls_words = []
for i in df_words:
    ls_words.append(i)
for i in range(len(ls_words)):
    ls_onlywords.append(ls_words[i].split("_")[0])
for i in range(len(ls_words)):
    ls_words[i] = ls_words[i].split("_")
df_scores = df['Score']
for i in range(len(ls_words)):
    ls_words[i].append(df_scores[i])

def changeabuse(sentence):
    words = list(sentence.split())
    sentiment_score = 0
    for i in words:
        for j in ls_words:
            if j[0] == i:
                sentiment_score = sentiment_score + j[-1]
                break
    if sentiment_score > 0:
        ls_m = list(sentence.split())
        for i in range(len(ls_m)):
            if ls_m[i] in ls_onlywords:
                ls_m[i] = build_n_gram()
        updated_message = ' '.join(ls_m)
        return updated_message
    else:
        return sentence

sentence = input()
print(changeabuse(sentence))