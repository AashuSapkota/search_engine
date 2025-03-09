import re
import numpy as np
import pandas as pd

import nltk
from nltk.tokenize import WhitespaceTokenizer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.naive_bayes import MultinomialNB

from sklearn.metrics import accuracy_score, confusion_matrix


import pickle

# reading dataset
dataset = pd.read_csv('./dataset/nyt_data.csv', sep='\t')

# merging the author, title and text into a single column
dataset['Text'] = dataset['Title'] + ' ' + dataset['Snippet']


# replacing the non-aplhabetical characters with whitespace
dataset['Text'] = dataset['Text'].str.replace('[^a-zA-Z]',' ')


# converting the word into smaller words
dataset['Text'] = [word.lower() for word in dataset['Text']]

# applying tokenization
dataset['Text'] = dataset['Text'].apply(nltk.tokenize.WhitespaceTokenizer().tokenize)


# removing stopwords
dataset['Text'] = dataset['Text'].apply(lambda words: [word for word in words if not word in stopwords.words('english')])



lemmatizer = WordNetLemmatizer()

def lemmatize_text(text):
    # lemmatize the wors from text
    return(lemmatizer.lemmatize(word) for word in text)

# applying lemmatization
dataset['Text'] = dataset['Text'].apply(lemmatize_text)



# Creating the 'lematized_title' column by joining the lemmatized words
dataset['lematized_title'] = dataset['Text'].apply(lambda words: ' '.join(words))


train_data = dataset['lematized_title'].values
target = dataset['Category'].values

# converting data into numerical values
vectorizer = TfidfVectorizer()
X_train = vectorizer.fit_transform(train_data)
Y_train = target

# training data into MultinomialNB
naive_clf = MultinomialNB()
naive_clf.fit(X_train, Y_train)


pickle.dump(naive_clf, open('text_clf.sav', 'wb'))
pickle.dump(vectorizer, open('text__vectorizer.sav', 'wb'))

