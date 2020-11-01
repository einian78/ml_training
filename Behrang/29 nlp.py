# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 12:19:57 2020

@author: koushb
"""

from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB 
from sklearn import metrics 
from nltk.corpus import stopwords
import string
from sklearn.feature_extraction.text import TfidfVectorizer



def text_process(mess):
    """
    Takes in a string of text, then performs the following:
    1. Remove all punctuation
    2. Remove all stopwords
    3. Returns a list of the cleaned text
    """
    STOPWORDS = stopwords.words('english') + ['u', 'ü', 'ur', '4', '2', 'im', 'dont', 'doin', 'ure']
    # Check characters to see if they are in punctuation
    nopunc = [char for char in mess if char not in string.punctuation]

    # Join the characters again to form the string.
    nopunc = ''.join(nopunc)
    
    # Now just remove any stopwords
    return ' '.join([word for word in nopunc.split() if word.lower() not in STOPWORDS])



sms=pd.read_csv('..\Data\Spam\spam.csv',encoding=('latin-1'))
sms=sms.iloc[:,[0,1]]
sms.columns=['label','text']

sms['target']=sms.label.map({'ham':0,'spam':1})
plt.hist(sms.target)
sms['text_len']=sms.text.apply(len)
sms['clean_text']=sms.text.apply(text_process)

sms[sms.target==1].text_len.plot.hist(alpha=0.8,color='blue',label='spam')
sms[sms.target==0].text_len.plot.hist(bins=30,alpha=0.5,color='red',label='Not spam')
plt.legend()
plt.xlim(0,400)


X=sms.clean_text
y=sms.target

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)


vect = CountVectorizer()
X_train_vec=vect.fit_transform(X_train)
X_test_vec=vect.transform(X_test)


NB=MultinomialNB()
NB.fit(X_train_vec,y_train)

y_pred=NB.predict(X_test_vec)
print(metrics.accuracy_score(y_test,y_pred))

print(metrics.confusion_matrix(y_test,y_pred))


tfidf=TfidfVectorizer()
X_train_tfidf=tfidf.fit_transform(X_train)
X_test_tfidf=tfidf.transform(X_test)

NB=MultinomialNB()
NB.fit(X_train_vec,y_train)

y_pred=NB.predict(X_test_vec)
print(metrics.accuracy_score(y_test,y_pred))

print(metrics.confusion_matrix(y_test,y_pred))
