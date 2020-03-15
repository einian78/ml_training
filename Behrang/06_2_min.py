# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 10:49:47 2020

@author: koushb
"""

from scipy.optimize import minimize


def bk_fun(x):
    r=x**2-8*x+7
    return(r)


print(bk_fun(12))

x0=[0]
res = minimize(bk_fun, x0)


