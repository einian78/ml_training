# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 10:10:55 2020

@author: koushb
"""


import matplotlib.pyplot as plt
import numpy as np

A=[[-6,3],[0,6],[2,2],[-4,-1]]

x=[]
y=[]
for p in A:
    x.append(p[0])
    y.append(p[1])

x.append(x[0])
y.append(y[0])
#x=[-6,0,2,-4,-6]
#y=[3,6,2,-1,3]

plt.plot(x,y)
plt.axes().set_aspect(1)  

def distance(p1,p2):
    dx=p1[0]-p2[0]
    dy=p1[1]-p2[1]
    r=np.sqrt(dx**2+dy**2)
    return(r)

def isrec(A):
    d1=distance(A[0], A[2])
    d2=distance(A[1], A[3])
    if d1==d2:
        return(True)
    else:
        return(False)


if isrec(A):
    print('It is a rectangle')
else:
    print('It is NOT a rectangle')

