# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 10:35:00 2020

@author: koushb
"""

import numpy as np
import pandas as pd
import sklearn.linear_model as lm
from sklearn.metrics import mean_squared_error as mse
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt


df_train=pd.read_csv("../Data/House Price Prediction/train.csv")
df_train['date']=pd.to_datetime(df_train['date'])
df_train['year']=df_train['date'].dt.year
df_train['month']=df_train['date'].dt.month

table_zip=pd.pivot_table(df_train,values='price',index='zipcode',aggfunc=np.mean)
table_zip=table_zip.sort_values('price')
table_zip['sorted_zipcode']=range(len(table_zip))
table_zip.sort_index(inplace=True)
plt.scatter(table_zip['sorted_zipcode'],table_zip['price'])
plt.show()

for i in range(len(df_train)):
    zc=df_train.loc[i,'zipcode']
    zp_new=table_zip.loc[zc,'sorted_zipcode']
    df_train.loc[i,'zipcode']=zp_new


#df_train['sorted_zipcode']=[table_zip.loc[i,'sorted_zipcode'] for i in df_train['zipcode']]

y=df_train['price']
X_train=df_train.drop(['price','id','date'],axis=1)
#df_train.drop(['price','id','date'],axis=1,inplace=True)

reg=lm.LinearRegression()
y_log=np.log(y)
reg.fit(X_train,y_log)

pred=reg.predict(X_train)
pred=np.exp(pred)
pred[pred>df_train['price'].max()]=df_train['price'].max()
pred[pred<df_train['price'].min()]=df_train['price'].min()

print('MSE is:',np.sqrt(mse(y,pred)))
print('R2 is:',r2_score(y,pred))


plt.scatter(y,pred,s=1)
plt.xlim(0,8000000)
plt.ylim(0,8000000)

df_test=pd.read_csv("../Data/House Price Prediction/test.csv")
df_test['date']=pd.to_datetime(df_test['date'])
df_test['year']=df_test['date'].dt.year
df_test['month']=df_test['date'].dt.month

for i in range(len(df_test)):
    zc=df_test.loc[i,'zipcode']
    zp_new=table_zip.loc[zc,'sorted_zipcode']
    df_test.loc[i,'zipcode']=zp_new


X_test=df_test.drop(['id','date'],axis=1)
pred=reg.predict(X_test)
pred=np.exp(pred)
A_pred=np.array([df_test['id'],pred]).T
df_pred=pd.DataFrame(A_pred,columns=['id','predict'])
df_pred.to_csv('test_predict.csv',index=False)






