# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 10:25:59 2020

@author: koushb
"""

import numpy as np
import matplotlib.pyplot as plt

x=[]
for i in range(10000):
    a=np.random.randint(1,7)
    x.extend([a]*a)
    
    

plt.hist(x,bins=20)




b=[]
for i in range(10000):  
    x=[]
    for i in range(200):
        a=np.random.randint(1,7)
        x.extend([a]*a)
        
    m=np.mean(x)
    b.append(m)

plt.hist(b,bins=20)

