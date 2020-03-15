# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 11:09:13 2020

@author: koushb
"""
import numpy as np
from scipy import optimize

def myfun(x):
    r=x**2-8*x+7
    return(r)


x0=[10]
sol = optimize.root(myfun, x0 )


import matplotlib.pyplot as plt

x=np.arange(0,10,0.1)
y=myfun(x)

plt.plot(x,y)

