# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 11:24:23 2020

@author: koushb
"""


def fact(n):
    r=1
    for i in range(n):
       r=r*(i+1)
    return(r)

print(fact(5))



def fact2(n):
    if n==1:
        r=1
    else:
        r=n*fact2(n-1)    
    return(r)



import time

start = time.time()
print(fact(20))
end = time.time()
print(end - start)


start = time.time()
print(fact2(20))
end = time.time()
print(end - start)