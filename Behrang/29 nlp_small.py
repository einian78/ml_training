# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 12:05:21 2020

@author: koushb
"""


from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd


simple_train = ['My name is Behrang', 'Behrang likes computer programming', 'Python is the best','Behrang behrang behrang']
vect = CountVectorizer()
simple_train_vec=vect.fit_transform(simple_train)
df=pd.DataFrame(simple_train_vec.toarray(),columns=vect.get_feature_names())
test=['Behrang is the best computer programmer']
a=vect.transform(test).toarray()

tfidf=TfidfVectorizer()
simple_train_vec_tfidf=tfidf.fit_transform(simple_train)
df_tfidf=pd.DataFrame(simple_train_vec_tfidf.toarray(),columns=vect.get_feature_names())

test=['Behrang is the best computer programmer']
a=tfidf.transform(test).toarray()
print(a)
