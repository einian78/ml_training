# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 18:53:55 2020

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


clf=lm.LogisticRegression(max_iter=1000)
clf.fit(X,y)

from sklearn.manifold import TSNE



ncomp=2
mytsne=TSNE(n_components=ncomp,n_iter=1000,perplexity=10)
X_TSNE=mytsne.fit_transform(X)

plt.scatter(X_TSNE[:,0],X_TSNE[:,1],s=0.3,c=y)
plt.colorbar()
plt.show()


clf=lm.LogisticRegression(max_iter=1000)
clf.fit(X_TSNE,y)
Pred=clf.predict(X_TSNE)
acc=accuracy_score(y,Pred)
print('accuracy score:',acc)


cm=confusion_matrix(y,Pred,normalize='true')
sns.heatmap(cm,annot=True)


