# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 11:14:21 2020

@author: koushb
"""

#sorting
lst=[1,6,4,3,8,9,1,5,8,8,7]

n=len(lst)
print(n)

for i in range(n):
    t1=lst[i]
    for j in range(n):
        t2=lst[j]
        if t1>t2:
            lst[j]=t1
            lst[i]=t2
            t1=t2

print(lst)   
        
