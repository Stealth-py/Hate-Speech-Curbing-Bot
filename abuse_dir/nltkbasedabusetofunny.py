from googleapiclient import discovery
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import subjectivity
from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.util import *
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import tokenize
from nltk.corpus import stopwords  
from nltk.tokenize import word_tokenize  
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
API_KEY=''

def abusetofunny(message):
    # Generates API client object dynamically based on service name and version.
    service = discovery.build('commentanalyzer', 'v1alpha1', developerKey=API_KEY)

    analyze_request = {
      'comment': { 'text': message },
      'requestedAttributes': {'TOXICITY': {}}
    }

    response = service.comments().analyze(body=analyze_request).execute()

    result = eval(json.dumps(response, indent=2))
    toxicity_score = result["attributeScores"]["TOXICITY"]['spanScores'][0]['score']['value']
    if toxicity_score < 0.5:
        return message
    else:
        stop_words = set(stopwords.words('english'))
        sentences = list(message.split('.'))
        ls_sentiment = []
        for i in range(len(sentences)):
            ls_words_remove_stop = list(sentences[i].split())
            for i in ls_words_remove_stop:
                if i in stop_words:
                    ls_words_remove_stop.remove(i)
            sentence_no_stop_words = ' '.join(ls_words_remove_stop)
            ss = sid.polarity_scores(sentence_no_stop_words)
            for k in sorted(ss):
                if k == 'compound':
                    ls_sentiment.append(ss[k])
        for m in range(len(sentences)):
            if ls_sentiment[m] > 0:
                pass
            else:
                ls_sentence = sentences[m].split()
                for j in range(len(ls_sentence)):
                    if ls_sentence[j].lower() in ls_onlywords:
                        ls_sentence[j] = list(build_n_gram().split())[0]
                    sentences[m] = ' '.join(ls_sentence)
        return ' '.join(sentences)
    

print(abusetofunny(str(input())))
