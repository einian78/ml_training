# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 10:57:33 2020

@author: koushb
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import mean_squared_error as mse
#from sklearn.metrics import r2_score



df=pd.read_csv("../Data/diabetes/diabetes.csv")

# define a condition for diabetes
def cond1(df):
    if df['target']>99.99:
        val = 1
    else:
        val = 0
    return val
    

varnames=list(df.columns)
varnames.remove('target')
X=df[varnames] 
#y=df['target']
#df['YN'] = [1 if df['target']>99.9 else 0]
df['YN'] = df.apply(cond1, axis=1)
y=df['YN'] 

logreg = LogisticRegression()


clf = logreg.fit(X,y)
clf.predict(X)
pred2 = logreg.predict(X)


err2 = mse(df['YN'], pred2)
      
print('Logistic regression Error', err2)
 

plt.scatter(df['target'], y, marker='+', linewidths=0.25)
plt.scatter(df['target'], pred2, marker='x', linewidths=0.25)
plt.title('Logistic Regression') 
plt.xlabel('target')
plt.ylabel('Diabetes of Not')
plt.show()


