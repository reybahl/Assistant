import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import base64
import string
import re
from io import StringIO
from collections import Counter
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer

stopwords = stopwords.words('english')

df = pd.read_csv('/home/pi/assistant/backend/data.csv')

# features = ['text']

# train = df[features]

tfidf = TfidfVectorizer(sublinear_tf = True, min_df =5, norm='l2', encoding = 'latin-1', ngram_range=(1, 2), stop_words = 'english')

features = tfidf.fit_transform(df.text).toarray()

labels = df.intent

print("done")