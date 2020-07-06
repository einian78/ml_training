# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 17:48:07 2020

@author: koushb
"""


import matplotlib.pyplot as plt
import cv2
import os
import numpy as np
from tqdm import tqdm

import sklearn.linear_model as lm
from sklearn.decomposition import PCA

from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import recall_score
from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve

import seaborn as sns

img = cv2.imread(r"C:\Users\koushb\OneDrive - Husky Energy\ML\data\mnist\4\img_3.jpg",0)/255
plt.imshow(img)

X=[]
y=[]
for digit in tqdm(range(10)):
    path="C:/Users/koushb/OneDrive - Husky Energy/ML/data/mnist/"+str(digit)+"/"
    files=os.listdir(path)
    for file in files[:500]:
        img = cv2.imread(path+file,0)/255
        img_flat=img.flatten()
        X.append(img_flat)
        y.append(digit)
        
X=np.array(X)
y=np.array(y)



X_test=[]
y_test=[]
for digit in tqdm(range(10)):
    path="C:/Users/koushb/OneDrive - Husky Energy/ML/data/mnist/"+str(digit)+"/"
    files=os.listdir(path)
    for file in files[500:1000]:
        img = cv2.imread(path+file,0)/255
        img_flat=img.flatten()
        X_test.append(img_flat)
        y_test.append(digit)
        
X_test=np.array(X_test)
y_test=np.array(y_test)




ncomp=2
mypca=PCA(n_components=ncomp)
X_PCA=mypca.fit_transform(X)

plt.scatter(X_PCA[:,0],X_PCA[:,1],c=y)
plt.colorbar()



ncomp=20
mypca=PCA(n_components=ncomp)
X_PCA=mypca.fit_transform(X)
X_test_PCA=mypca.transform(X_test)


plt.plot(mypca.explained_variance_ratio_)
plt.show()


plt.plot(np.cumsum(mypca.explained_variance_ratio_))

clf=lm.LogisticRegression(max_iter=1000)
clf.fit(X_PCA,y)

Pred=clf.predict(X_test_PCA)
acc=accuracy_score(y_test,Pred)
print('accuracy score:',acc)


cm=confusion_matrix(y_test,Pred,normalize='true')
sns.heatmap(cm,annot=True)

