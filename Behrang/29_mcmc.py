# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 13:32:48 2020

@author: koushb
"""

import numpy as np

p={'S':0.9,
   'R':0.3}

ndays=100000
Today='R'
days=[]
for i in range(ndays):
    r=np.random.uniform(0,1)
    if Today=='S':
        if  r>p[Today]:
            Nextday='R'
        else:
            Nextday='S'
    else:
        if  r>p[Today]:
            Nextday='S'
        else:
            Nextday='R'
    Today=Nextday
    if Today=='S': 
        days.append(1)
    else:
        days.append(0)
        
days=np.array(days)
print(days[100:].mean())
