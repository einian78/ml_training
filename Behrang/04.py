# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 10:16:50 2020

@author: koushb
"""

a=input('enter a number')

lst=[]
for i in range(len(a)):
    #print(a[i])   
    lst.append(int(a[i]))

lst.sort()
#print(lst)

b=0
k=1
for i in lst:
   b=b+k*i
   k=k*10

print(b)
lst.sort(reverse=False)
for i in range(len(lst)):
    n=lst[i] 
    if n !=0:
        lst[i]=lst[0]
        lst[0]=n
        break


b=0
k=1
for i in lst:
   b=b*10+i

print(b)