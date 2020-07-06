# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 17:59:26 2020

@author: koushb
"""
import numpy as np
import pandas as pd
import sklearn.linear_model as lm
from sklearn.metrics import mean_squared_error as mse
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

df=pd.read_csv("../Data/diabetes/diabetes.csv")

y=df['target']

X_train1=df.drop('target',axis=1)
reg1=lm.LinearRegression()

reg1.fit(X_train1,y)

Pred1=reg1.predict(X_train1)
print('RMSE is:',round(np.sqrt(mse(y,Pred1)),2))
print('R2 is:',round(r2_score(y,Pred1),2))

plt.plot(y,Pred1,'.')
plt.scatter(y,Pred1)
plt.show()
###################################################
poly=PolynomialFeatures(2)
X_train2=poly.fit_transform(X_train1)
polynames=poly.get_feature_names(X_train1.columns)
X_train2=pd.DataFrame(X_train2,columns=polynames)
scaleit=StandardScaler()
X_train3=scaleit.fit_transform(X_train2)
X_train3=pd.DataFrame(X_train3,columns=X_train2.columns)

reg3=lm.LinearRegression()
reg3.fit(X_train3,y)
Pred3=reg3.predict(X_train3)
print('RMSE is:',round(np.sqrt(mse(y,Pred3)),2))
print('R2 is:',round(r2_score(y,Pred3),2))


plt.plot(y,Pred3,'.')
plt.scatter(y,Pred3)
plt.show()
###################################################

ncomp=10
mypca=PCA(n_components=ncomp)
X_train4=mypca.fit_transform(X_train3)

reg4=lm.LinearRegression()
reg4.fit(X_train4,y)
Pred4=reg4.predict(X_train4)
print('RMSE is:',round(np.sqrt(mse(y,Pred4)),2))
print('R2 is:',round(r2_score(y,Pred4),2))


plt.plot(y,Pred4,'.')
plt.scatter(y,Pred4)
plt.show()

plt.plot(mypca.explained_variance_ratio_)
plt.show()


plt.plot(np.cumsum(mypca.explained_variance_ratio_))









