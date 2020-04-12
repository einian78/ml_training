# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 20:28:30 2020

@author: Maryam
"""




#import numpy as np
import pandas as pd
import itertools as it
from tqdm import tqdm

import sklearn.linear_model as lm
from sklearn.metrics import mean_squared_error as mse
#from sklearn.metrics import r2_score

df =pd.read_csv("../Maryam/HPtrain.csv")
varnames = list(df.columns)
varnames.remove('id')    
varnames.remove('date')
varnames.remove('zipcode')
varnames.remove('long')
varnames.remove('lat')

varnames.remove('sqft_lot')
varnames.remove('condition')
varnames.remove('yr_built')
varnames.remove('sqft_lot15')

varnames.remove('price')

#df.drop(['id', 'date', 'price'])
y = df["price"]

#cases = list(it.combinations(varnames,3))

reg = lm.LinearRegression()

err=90000000000


for k in range(3,7):
    cases = list(it.combinations(varnames, k))
    #print(cases)
    print(k)
    
    for i in tqdm(cases):
        
        X = df[list(i)]
        reg.fit(X,y)
        Pred = reg.predict(X)
        if mse(y, Pred) < err:
            err = mse(y, Pred)
            l = list(i)
            print(l)
        
print(l)
print('Best MSE is: ', err)



'''
cases = list(it.combinations(varnames, 3))

print(cases)

for i in tqdm(cases):
    X = df[list(i)]
    reg.fit(X,y)
    Pred = reg.predict(X)
    if mse(y, Pred) < err:
        err = mse(y, Pred)
        l = list(i)
        
#print(l)
print('Best MSE is: ', err)
'''



