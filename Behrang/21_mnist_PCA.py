# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 18:23:19 2020

@author: koushb
"""
import matplotlib.pyplot as plt
import numpy as np
import cv2
import os
from tqdm import tqdm
import sklearn.linear_model as lm

from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

import seaborn as sns

img_name='C:/Users/koushb/OneDrive - Husky Energy/ML/data/mnist/2/img_302.jpg'
img_np=cv2.imread(img_name,0)/255
plt.imshow(img_np)

X=[]
y=[]

for d in tqdm(range(0,10)):
    path='C:/Users/koushb/OneDrive - Husky Energy/ML/data/mnist/'+str(d)
    #print(path)
    files=os.listdir(path)
    for img_name in files[:500]:
        img_np=cv2.imread(path+'/'+img_name,0)/255.
        img_np=img_np.flatten()
        X.append(img_np)
        y.append(d)

X=np.array(X)
y=np.array(y)

X_test=[]
y_test=[]
for d in tqdm(range(0,10)):
    path='C:/Users/koushb/OneDrive - Husky Energy/ML/data/mnist/'+str(d)
    #print(path)
    files=os.listdir(path)
    for img_name in files[500:600]:
        img_np=cv2.imread(path+'/'+img_name,0)/255.
        img_np=img_np.flatten()
        X_test.append(img_np)
        y_test.append(d)

X_test=np.array(X_test)
y_test=np.array(y_test)



clf=lm.LogisticRegression(max_iter=1000)
clf.fit(X,y)

Pred=clf.predict(X_test)
acc=accuracy_score(y_test,Pred)
print('accuracy score:',acc)

img_name='C:/Users/koushb/OneDrive - Husky Energy/ML/data/mnist/7/img_136.jpg'
img_np=cv2.imread(img_name,0)/255
plt.imshow(img_np)
img_np=img_np.flatten()
print(clf.predict(img_np.reshape(1,-1))[0])

cm=confusion_matrix(y_test,Pred,normalize='true')
sns.heatmap(cm,annot=True)






from sklearn.decomposition import PCA
ncomp=784
mypca=PCA(n_components=ncomp)
X_PCA=mypca.fit_transform(X)


plt.plot(mypca.explained_variance_ratio_)
plt.show()




ncomp=100
mypca=PCA(n_components=ncomp)
X_PCA=mypca.fit_transform(X)
X_test_PCA=mypca.transform(X_test)

clf=lm.LogisticRegression(max_iter=1000)
clf.fit(X_PCA,y)

Pred=clf.predict(X_test_PCA)
acc=accuracy_score(y_test,Pred)
print('accuracy score:',acc)

cm=confusion_matrix(y_test,Pred,normalize='true')
sns.heatmap(cm,annot=True)





ncomp=2
mypca=PCA(n_components=ncomp)
X_PCA=mypca.fit_transform(X)

plt.scatter(X_PCA[:,0],X_PCA[:,1],s=0.3,c=y)
plt.colorbar()
plt.show()


