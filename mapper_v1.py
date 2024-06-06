#!/usr/bin/python3
# -*-coding:utf-8 -*
import sys 
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
en_stopwords = stopwords.words('english')

  
for line in sys.stdin: 
    lower = line.apply(lambda x: str(x).lower())
    lower = ' '.join([word for word in lower.split() if word not in en_stopwords])
    words = lower.str.strip().str.replace(r'[^\w\s]', '', regex=True)
    for word in words:
        print('%s\t%s' % (word, 1))
