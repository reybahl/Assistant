import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
from io import StringIO
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer

class IntentClassifier:
    def __init__(self):
        self.data = pd.read_csv('intentclassification/data.csv')
        self.train()

    def train(self):
        X_train, y_train= self.data['text'], self.data['intent']
        self.count_vect = CountVectorizer()
        X_train_counts = self.count_vect.fit_transform(X_train)
        tfidf_transformer = TfidfTransformer()
        X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
        # self.clf = MultinomialNB().fit(X_train_tfidf, y_train)
        self.svm = LinearSVC().fit(X_train_tfidf, y_train)
    
    def predict(self, text):
        return self.svm.predict(self.count_vect.transform([text]))[0]