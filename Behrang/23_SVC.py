# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 17:53:36 2020

@author: koushb
"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVC

X=np.array([[4,3,6,6,14,13,16],[5,7,8,5,15,17,18]]).T
y=np.array([0,0,0,1,1,1,1])


X=np.array([[4,3,6,14,13,16],[5,7,8,15,17,18]]).T
y=np.array([0,0,0,1,1,1])

nx=np.array([[3,3],[10,10],[18,18]])

plt.scatter(X[:,0], X[:,1],c=y)
plt.scatter(nx[:,0],nx[:,1],c='b',marker='*')
plt.xlim(0,20)
plt.ylim(0,20)

clf=SVC(kernel='linear',C=1)
clf.fit(X,y)

print(clf.predict(nx))



xlim = (0,20)
ylim = (0,20)

# create grid to evaluate model
xx = np.linspace(xlim[0], xlim[1], 30)
yy = np.linspace(ylim[0], ylim[1], 30)
YY, XX = np.meshgrid(yy, xx)
xy = np.vstack([XX.ravel(), YY.ravel()]).T
Z = clf.decision_function(xy).reshape(XX.shape)

# plot decision boundary and margins
plt.contour(XX, YY, Z, colors='k', levels=[-1, 0, 1], alpha=0.5,
           linestyles=['--', '-', '--'])
# plot support vectors
plt.scatter(clf.support_vectors_[:, 0], clf.support_vectors_[:, 1], s=100,
           linewidth=1, facecolors='none', edgecolors='k')





