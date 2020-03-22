# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 11:10:45 2020

@author: koushb
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize 

a=10
def f(x):
    y=(a/x)**x
    return(-y)

x=np.arange(0.001,10,0.001)
y=f(x)
plt.plot(x,y)


res=minimize(f,[0.001],bounds=[(0.001,None)])
print(res.x[0])
print(a/np.e)
