# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 23:23:56 2020

@author: Maryam
"""


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score

data = pd.read_csv("../Data/diabetes/diabetes.csv")
print(data.head())
print(data.describe())
print(data.info())

original_data = data.copy()



data.loc[data['AGE'] <= 16, 'AGE'] = 0
data.loc[(data['AGE'] > 16) & (data['AGE'] <= 32), 'AGE'] = 1
data.loc[(data['AGE'] > 32) & (data['AGE'] <= 48), 'AGE'] = 2
data.loc[(data['AGE'] > 48) & (data['AGE'] <= 64), 'AGE'] = 3
data.loc[data['AGE'] > 64, 'AGE'] = 4

data.loc[data['BMI'] <= 20, 'BMI'] = 0
data.loc[(data['BMI'] > 20) & (data['BMI'] <= 30), 'BMI'] = 1
data.loc[data['BMI'] > 30, 'BMI'] = 2

data.loc[data['BP'] <= 80, 'BP'] = 0
data.loc[(data['BP'] > 80) & (data['BP'] <= 110), 'BP'] = 1
data.loc[data['BP'] > 110, 'BP'] = 2

data.loc[data['S1'] <= 160, 'S1'] = 0
data.loc[(data['S1'] > 160) & (data['S1'] <= 220), 'S1'] = 1
data.loc[data['S1'] > 220, 'S1'] = 2

data.loc[data['S2'] <= 70, 'S2'] = 0
data.loc[(data['S2'] > 70) & (data['S2'] <= 140), 'S2'] = 1
data.loc[data['S2'] > 140, 'S2'] = 2

data.loc[data['S3'] <= 40, 'S3'] = 0
data.loc[(data['S3'] > 40) & (data['S3'] <= 75), 'S3'] = 1
data.loc[data['S3'] > 75, 'S3'] = 2

data.loc[data['S4'] <= 3, 'S4'] = 0
data.loc[(data['S4'] > 3) & (data['S4'] <= 6), 'S4'] = 1
data.loc[data['S4'] > 6, 'S4'] = 2

data.loc[data['S5'] <= 4.5, 'S5'] = 0
data.loc[(data['S5'] > 4.5) & (data['S5'] <= 5.5), 'S5'] = 1
data.loc[data['S5'] > 5.5, 'S5'] = 2

data.loc[data['S6'] <= 80, 'S6'] = 0
data.loc[(data['S6'] > 80) & (data['S6'] <= 100), 'S6'] = 1
data.loc[data['S6'] > 100, 'S6'] = 2

data.loc[data['target'] <=150, 'target'] = 0
data.loc[data['target'] > 150, 'target'] = 1


data['target'] = data['target'].astype(int)
data['AGE'] = data['AGE'].astype(int)
data['BMI'] = data['BMI'].astype(int)
data['BP'] = data['BP'].astype(int)
data['S1'] = data['S1'].astype(int)
data['S2'] = data['S2'].astype(int)
data['S3'] = data['S3'].astype(int)
data['S4'] = data['S4'].astype(int)
data['S5'] = data['S5'].astype(int)
data['S6'] = data['S6'].astype(int)    
    
print(data.head())

varnames=list(data.columns)
varnames.remove('target')
X=data[varnames]
y=data['target']


clf = DecisionTreeClassifier(random_state=0, max_leaf_nodes=8, max_depth=6)
clf.fit(X, y)


pred = clf.predict(X)

acc = accuracy_score(y, pred)
print('Accuracy of Decision Tree Classifier :', acc)

cv = cross_val_score(clf, X, y, cv=5)
print('Cross Validation score is: ', cv)