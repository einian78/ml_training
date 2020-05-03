# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 10:35:00 2020


"""

import numpy as np
import pandas as pd
import sklearn.linear_model as lm
from sklearn.metrics import mean_squared_error as mse
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import StandardScaler

df_train=pd.read_csv("../Data/House Price Prediction/train.csv")
#self created testing:
#df_train = df_train.head(8000)

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

#linear
y=df_train['price']
X_train1=df_train.drop(['price','id','date'],axis=1)

reg1=lm.LinearRegression()
y_log=np.log(y)
reg1.fit(X_train1,y_log)

Pred1=reg1.predict(X_train1)
Pred1=np.exp(Pred1)
Pred1[Pred1>df_train['price'].max()]=df_train['price'].max()
Pred1[Pred1<df_train['price'].min()]=df_train['price'].min()
print('Linear')
print('RMSE is:',round(np.sqrt(mse(y,Pred1)),2))
print('R2 is:',round(r2_score(y,Pred1),2))

plt.plot(y,Pred1,'.')
plt.scatter(y,Pred1)
plt.show()


##############################
#poly
poly=PolynomialFeatures(2)
X_train2=poly.fit_transform(X_train1)
polynames=poly.get_feature_names(X_train1.columns)
X_train2=pd.DataFrame(X_train2,columns=polynames)


reg2=lm.LinearRegression()
y_log=np.log(y)
reg2.fit(X_train2,y_log)

Pred2=reg2.predict(X_train2)
Pred2=np.exp(Pred2)
Pred2[Pred2>df_train['price'].max()]=df_train['price'].max()
Pred2[Pred2<df_train['price'].min()]=df_train['price'].min()
print('Polynomial fit')
print('RMSE is:',round(np.sqrt(mse(y,Pred2)),2))
print('R2 is:',round(r2_score(y,Pred2),2))

plt.plot(y,Pred2,'.')
plt.scatter(y,Pred2)
plt.show()

##############################
#linear with rescaling the original train data
scaleit=StandardScaler()

X_train3=scaleit.fit_transform(X_train1)
X_train3=pd.DataFrame(X_train3,columns=X_train1.columns)

reg3=lm.LinearRegression()
y_log = np.log(y)
reg3.fit(X_train3,y_log)

Pred3=reg3.predict(X_train3)
Pred3=np.exp(Pred3)
Pred3[Pred3>df_train['price'].max()]=df_train['price'].max()
Pred3[Pred3<df_train['price'].min()]=df_train['price'].min()
print('Linear fit with scaling the original train data')
print('RMSE is:',round(np.sqrt(mse(y,Pred3)),2))
print('R2 is:',round(r2_score(y,Pred3),2))


plt.plot(y,Pred3,'.')
plt.scatter(y,Pred3)
plt.show()

#########################
#poly with rescaling the poly train data
scaleit=StandardScaler()

X_train4=scaleit.fit_transform(X_train2)
X_train4=pd.DataFrame(X_train4,columns=polynames)


reg4=lm.LinearRegression()
y_log = np.log(y)
reg4.fit(X_train4,y_log)

Pred4=reg4.predict(X_train4)
Pred4=np.exp(Pred4)
Pred4[Pred4>df_train['price'].max()]=df_train['price'].max()
Pred4[Pred4<df_train['price'].min()]=df_train['price'].min()
print('Polynomial fit with scaling the polynomial train data')
print('RMSE is:',round(np.sqrt(mse(y,Pred4)),2))
print('R2 is:',round(r2_score(y,Pred4),2))


plt.plot(y,Pred4,'.')
plt.scatter(y,Pred4)
plt.show()


##############################
#Test:
df_test=pd.read_csv("../Data/House Price Prediction/test.csv")
#df_test=pd.read_csv("../Data/House Price Prediction/train.csv")
#df_test = df_test.tail(500)
#df_test.reset_index(inplace=True,drop=True)
#y2 = df_test['price']


df_test['date']=pd.to_datetime(df_test['date'])
df_test['year']=df_test['date'].dt.year
df_test['month']=df_test['date'].dt.month


for i in range(len(df_test)):
    zc=df_test.loc[i,'zipcode']
    zp_new=table_zip.loc[zc,'sorted_zipcode']
    df_test.loc[i,'zipcode']=zp_new



#X_test1=df_test.drop(['id','date','price'],axis=1)
X_test1=df_test.drop(['id','date'],axis=1)


scaleit=StandardScaler()
X_test3=scaleit.fit_transform(X_test1)
X_test3=pd.DataFrame(X_test3,columns=X_test1.columns)


X_test2=poly.fit_transform(X_test1)
polynames=poly.get_feature_names(X_test1.columns)
X_test2=pd.DataFrame(X_test2,columns=polynames)

scaleit=StandardScaler()
X_test4=scaleit.fit_transform(X_test2)
X_test4=pd.DataFrame(X_test4,columns=polynames)


Pred=reg2.predict(X_test2)
Pred=np.exp(Pred)


A_pred=np.array([df_test['id'],Pred]).T
df_pred=pd.DataFrame(A_pred,columns=['id','predict'])
df_pred.to_csv('test_predict.csv',index=False)

#print('Test:')
#print('RMSE is:',round(np.sqrt(mse(y2,Pred)),2))
#print('R2 is:',round(r2_score(y2,Pred),2))

#plt.plot(y2,Pred,'.')
#plt.scatter(y2,Pred)
#plt.show()


