# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 12:10:49 2020

@author: koushb
"""

import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error as mse
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
from sklearn.model_selection import cross_val_score

import lightgbm as lgbm
from sklearn.model_selection import GridSearchCV

from sklearn.model_selection import train_test_split

df_train=pd.read_csv("../Data/House Price Prediction/train.csv")
df_train['date']=pd.to_datetime(df_train['date'])
df_train['year']=df_train['date'].dt.year
df_train['month']=df_train['date'].dt.month


y=df_train['price']
X=df_train.drop(['price','id','date'],axis=1)

reg=lgbm.LGBMRegressor(
    objective='regression',
    boosting_type='gbdt',
    learning_rate=0.1,
    num_leaves=31,
    n_estimators=25,
    min_split_gain=0.1,
    subsample=0.6,
    colsample_bytree=0.8,
    reg_alpha=5,
    reg_lambda=5,
    )



reg.fit(X,y)
pred=reg.predict(X)
pred[pred>df_train['price'].max()]=df_train['price'].max()
pred[pred<df_train['price'].min()]=df_train['price'].min()
print('MSE is:',np.sqrt(mse(y,pred)))
print('R2 is:',r2_score(y,pred))
plt.scatter(y,pred,s=1)
plt.xlim(0,8000000)
plt.ylim(0,8000000)
scores=cross_val_score(reg,X=X,y=y,cv=5,scoring='r2')
print(scores)
print('cv_mean:',round(scores.mean(),2))
print('cv_std:',round(scores.std(),2))

gridparam={
    'num_leaves':[30,50],
    'boosting_type':['gbdt','dart'],
    'learning_rate':[0.1,0.01],
    'n_estimators':[25,50],
    'subsample':[0.7,0.9],
    'colsample_bytree':[0.8,0.9],
    'reg_alpha':[0,5,10],
    'reg_lambda':[0,5,10]
  
    }

grid=GridSearchCV(reg,gridparam,cv=4,verbose=1)
grid.fit(X,y)

print(grid.best_score_)
print(grid.best_params_)


reg=lgbm.LGBMRegressor(
    objective='regression',
    boosting_type=grid.best_params_['boosting_type'],
    learning_rate=grid.best_params_['learning_rate'],
    num_leaves=grid.best_params_['num_leaves'],
    n_estimators=grid.best_params_['n_estimators'],
    min_split_gain=0.1,
    subsample=grid.best_params_['subsample'],
    colsample_bytree=grid.best_params_['colsample_bytree'],
    reg_alpha=grid.best_params_['reg_alpha'],
    reg_lambda=grid.best_params_['reg_lambda'],
    )



reg.fit(X,y)
pred=reg.predict(X)
pred[pred>df_train['price'].max()]=df_train['price'].max()
pred[pred<df_train['price'].min()]=df_train['price'].min()
print('MSE is:',np.sqrt(mse(y,pred)))
print('R2 is:',r2_score(y,pred))
plt.scatter(y,pred,s=1)
plt.xlim(0,8000000)
plt.ylim(0,8000000)
scores=cross_val_score(reg,X=X,y=y,cv=5,scoring='r2')
print(scores)
print('cv_mean:',round(scores.mean(),2))
print('cv_std:',round(scores.std(),2))

#######################################################
params = {
    'application': 'regression', 
#     'num_class' : 1, # used for multi-classes
    'boosting': 'gbdt', # traditional gradient boosting decision tree
    'num_iterations': 1000, 
    'learning_rate': 0.05,
    'num_leaves': 62,
    'device': 'cpu', # you can use GPU to achieve faster learning
    'max_depth': -1, # <0 means no limit
    'max_bin': 510, # Small number of bins may reduce training accuracy but can deal with over-fitting
    'lambda_l1': 5, # L1 regularization
    'lambda_l2': 10, # L2 regularization
    'metric' : 'rmse',
    'subsample_for_bin': 200, # number of samples for constructing bins
    'subsample': 0.8, # subsample ratio of the training instance
    'colsample_bytree': 0.8, # subsample ratio of columns when constructing the tree
    'min_split_gain': 0.5, # minimum loss reduction required to make further partition on a leaf node of the tree
    'min_child_weight': 1, # minimum sum of instance weight (hessian) needed in a leaf
    'min_child_samples': 5# minimum number of data needed in a leaf
}



X_train,X_valid,y_train,y_valid=train_test_split(X,y,test_size=0.2)
d_train=lgbm.Dataset(X_train,label=y_train)
d_valid=lgbm.Dataset(X_valid,label=y_valid)

model=lgbm.train(params,train_set=d_train,num_boost_round=1000,valid_sets=d_valid,early_stopping_rounds=50,verbose_eval=4)

