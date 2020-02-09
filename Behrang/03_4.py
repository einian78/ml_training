# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 11:24:49 2020

@author: koushb
"""

import pandas as pd
from sklearn import  linear_model as lm
from sklearn.metrics import mean_squared_error as mse
from sklearn.metrics import r2_score as r2
import matplotlib.pyplot as plt

lst=[1,6,4,3,8,9,1,5,8,8,7]


a=np.mean(lst)
print(a)

df_bk=pd.read_csv("diabetes.csv")

#var_names=['AGE', 'SEX', 'BMI', 'BP', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6']
var_names=list(df_bk.columns)
var_names.remove('target')

#for c in var_names:    
#    df_bk[c+'^2']=df_bk[c]*df_bk[c]


var_names=list(df_bk.columns)
var_names.remove('target')

X=df_bk[var_names].values
y=df_bk['target'].values

reg = lm.LinearRegression()
reg.fit(X,y)

pred=reg.predict(X)

plt.figure(figsize=(20,20))
#plt.plot(pred,y,'.')
plt.scatter(pred,y)
plt.show()

my_mse=mse(y,pred)
my_r2=r2(y,pred)

print('MSE=',my_mse)
print('r2=',my_r2)



