# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 10:46:19 2020

@author: koushb
"""

import numpy as np


def f1(n):
    r1=(-1)**n
    r2=(2*n+1)
    r=r1/r2
    return(r)

m=100000
p=0
for i in range(m):
    p=p+f1(i)
p=p*4
print(p)



def f2(i):
    r=1/i**2
    return(r)

m=10000
p=0
for i in range(1,m):
    p=p+f2(i)

p=np.sqrt(p*6)

print(p)
