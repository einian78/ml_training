# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 10:55:27 2020

@author: koushb
"""

import numpy as np


def pow(x,n):
    return(x**n)

def fact(n):
    r=1
    for i in range(1,n+1):
        r=r*i
    return(r)

def f1(x,n):
    r=pow(x,n)/fact(n)
    return(r)

m=100
ex=1
x=2
for i in range(1,m):
    ex=ex+f1(x,i)

print(ex)




#####################################

x=1
m=1000
ex=1
y=x
for i in range(1,m):      
   y=y*(x/i)
   ex=ex+y
print(ex)

