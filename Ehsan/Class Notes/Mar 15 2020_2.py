# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import scipy as sp
from scipy.optimize import minimize
from scipy import optimize
import time
import matplotlib.pyplot as plt



def fun(x):
    r = x**2 -8*x + 7
    return(r)

start = time.time()
x0 = [10]
#res = minimize(fun,x0)
#print(res)
res2 = optimize.root(fun,x0)
print(res2)
end = time.time()
print(end - start)

start = time.time()
coeff = [1,-8,7]
res3 = np.roots(coeff)
#print(res3)
end = time.time()
print(end - start)

x = np.arange(0,10,0.1)
y = fun(x)
plt.plot(x,y)

#e and pi fastest (recursive?) up to 20 taylor series terms