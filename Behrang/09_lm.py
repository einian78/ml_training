# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 10:29:31 2020

@author: koushb
"""


import numpy as np
import pandas as pd
import itertools as it
#from sklearn.linear_model import LinearRegression
import sklearn.linear_model as lm
from sklearn.metrics import mean_squared_error as mse
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt

diabetes=pd.read_csv("../Data/diabetes/diabetes.csv")

varnames=list(diabetes.columns)

varnames.remove('target')
#list(it.combinations(varnames,3))

#X=diabetes[['AGE','SEX','BMI']]
X=diabetes[varnames]
y=diabetes['target']

reg=lm.LinearRegression()

reg.fit(X,y)

Pred=reg.predict(X)
print('MSE is:',mse(y,Pred))
print('R2 is:',r2_score(y,Pred))

plt.plot(y,Pred,'.')
plt.scatter(y,Pred)

