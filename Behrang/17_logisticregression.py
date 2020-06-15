# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 18:05:57 2020

@author: koushb
"""

import pandas as pd
import sklearn.linear_model as lm
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import recall_score
from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve
import seaborn as sns

df=pd.read_csv("../Data/diabetes/diabetes.csv")

varnames=list(df.columns)

varnames.remove('target')
X=df[varnames]
y=df['target']

y[y<=100]=0
y[y>100]=1

clf=lm.LogisticRegression(max_iter=1000)
clf.fit(X,y)

Pred=clf.predict(X)
acc=accuracy_score(y,Pred)
print('accuracy score:',acc)

rcl=recall_score(y,Pred)
print('recall score:',rcl)



pred_prob=clf.predict_proba(X)
auc=roc_auc_score(y,pred_prob[:,1])
print('auc score:',auc)

fpr, tpr, thresholds=roc_curve(y,pred_prob[:,1])
plt.plot(fpr,tpr)
plt.plot([0,1],[0,1])

cm=confusion_matrix(y,Pred)
plt.imshow(cm,cmap='binary')

cm=confusion_matrix(y,Pred,normalize='true')

sns.heatmap(cm,annot=True)
