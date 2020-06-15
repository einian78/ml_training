# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 19:08:55 2020

@author: koushb
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn import neighbors

np.random.seed(0)

X = np.sort(5 * np.random.rand(40, 1), axis=0)
T = np.linspace(0, 5, 500).reshape(-1,1)
y = np.sin(X).ravel()

plt.plot(X,y)
y[::5] += 1 * (0.5 - np.random.rand(8))
plt.plot(X,y,'*')

n_neighbors = 40
knn = neighbors.KNeighborsRegressor(n_neighbors, weights='uniform')
knn.fit(X, y)
pred=knn.predict(T)

plt.scatter(X, y, color='darkorange', label='data')
plt.plot(T, pred, color='navy', label='prediction')
plt.show()


knn = neighbors.KNeighborsRegressor(n_neighbors, weights='distance')
knn.fit(X, y)
pred=knn.predict(T)

plt.scatter(X, y, color='darkorange', label='data')
plt.plot(T, pred, color='navy', label='prediction')
plt.show()


            
        