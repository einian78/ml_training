# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 10:06:34 2020

@author: koushb
"""


n=int(input('enter a number'))
lst=[]
for i in range(n):
    lst.append(float(input()))
    

s=0
ss=0
for i in lst:
    s=s+i

m=s/n
print(m)

for i in lst:
    ss=ss+(i-m)**2

print(ss/(n-1))


s=0
ss=0
for i in range(n):
    a=float(input())
    s=s+a
    ss=ss+a**2
    
m=s/n
print(m)


