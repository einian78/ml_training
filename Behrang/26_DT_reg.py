# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 19:04:33 2020

@author: koushb
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import BaggingRegressor

np.random.seed(0)

X = np.sort(5 * np.random.rand(40, 1), axis=0)
T = np.linspace(0, 5, 500).reshape(-1,1)
y = np.sin(X).ravel()

plt.plot(X,y)
y[::5] += 1 * (0.5 - np.random.rand(8))
plt.plot(X,y,'*')

dt=DecisionTreeRegressor(max_depth=6,min_samples_leaf=5)
dt.fit(X, y)
pred=dt.predict(T)

plt.scatter(X, y, color='darkorange', label='data')
plt.plot(T, pred, color='navy', label='prediction')
plt.show()


reg=BaggingRegressor(dt,n_estimators=100,max_samples=0.9,max_features=1)
reg.fit(X, y)
pred=reg.predict(T)
plt.scatter(X, y, color='darkorange', label='data')
plt.plot(T, pred, color='navy', label='prediction')
plt.show()

