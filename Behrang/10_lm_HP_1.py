# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 09:56:57 2020

@author: koushb
"""

import numpy as np
import pandas as pd
import sklearn.linear_model as lm
from sklearn.metrics import mean_squared_error as mse
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt


df_train=pd.read_csv("../Data/House Price Prediction/train.csv")

varnames=list(df_train.columns)
varnames.remove('price')
varnames.remove('id')
varnames.remove('date')
varnames.remove('zipcode')

X_train=df_train[varnames]
y=df_train['price']

reg=lm.LinearRegression()

reg.fit(X_train,y)

pred=reg.predict(X_train)
print('MSE is:',np.sqrt(mse(y,pred)))
print('R2 is:',r2_score(y,pred))


plt.scatter(y,pred,s=1)

df_test=pd.read_csv("../Data/House Price Prediction/test.csv")
X_test=df_test[varnames]
pred=reg.predict(X_test)

A_pred=np.array([df_test['id'],pred]).T
df_pred=pd.DataFrame(A_pred,columns=['id','predict'])
df_pred.to_csv('test_predict.csv',index=False)
