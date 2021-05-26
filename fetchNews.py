from newsapi import NewsApiClient
import json
import sys, tweepy
import re
import string
import requests
import nltk

# Init
newsapi = NewsApiClient(api_key='80979f75db4c46198e1fb95d6238d0b1')

query = "Phoenix"

all_articles = newsapi.get_everything(q=query,
                                      from_param='2020-07-15',
                                      to='2017-07-16',
                                      language='en',
                                      sort_by='relevancy')
js = json.dumps(all_articles)

f = open("outputFile.txt", "a")

for val in json.loads(js)["articles"]:
    descrip = val["description"]
    table = str.maketrans('', '', string.punctuation)
    s = re.split(r'\W+', descrip)
    stripped = [w.translate(table) for w in s]
    words = [word.lower() for word in stripped]
    for word in words:
        f.write("(news)"+word+"\n")
