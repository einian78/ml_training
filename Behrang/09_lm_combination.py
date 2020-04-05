# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 10:57:33 2020

@author: koushb
"""

import pandas as pd
import itertools as it
from tqdm import tqdm
import sklearn.linear_model as lm
from sklearn.metrics import mean_squared_error as mse
from sklearn.metrics import r2_score

df=pd.read_csv("../Data/diabetes/diabetes.csv")
varnames=list(df.columns)
varnames.remove('target')
y=df['target']

cases=list(it.combinations(varnames,3))
reg=lm.LinearRegression()

err=1000000
for i in tqdm(cases):
  X=df[list(i)] 
  reg.fit(X,y)
  Pred=reg.predict(X)
  if mse(y,Pred)<err:
      err=mse(y,Pred)
      l=list(i)
      
print(l)      
print('Best MSE is:',err)
  