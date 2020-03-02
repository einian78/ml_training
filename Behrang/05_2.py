# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 11:05:23 2020

@author: koushb
"""

import numpy as np
import matplotlib.pyplot as plt

a=np.random.randint(1,7,10000)

plt.hist(a,bins=3,range=(1,7))
y = np.bincount(a)
print(y)




b=[]
for i in range(100000):
    a=np.random.randint(1,7,100)
    m=np.mean(a)
    b.append(m)

plt.hist(b,bins=20)

