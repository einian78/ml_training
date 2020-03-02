# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 10:15:28 2020

@author: koushb
"""

import numpy as np

lst=[10,9,38,6,765]
a=np.array(lst)

print(a[0])

b=a[0:2]
print(b)

c=a[1:]

d=a[-2]

lst=[[10,9,38,6,765],[-9,3,-5,1,9]]
a=np.array(lst)

print(a.shape)

c=a[1,:]
print(c)


print(a[1:3,2:4])

d=a[1:3,:]
print(d[0,2:4])


lst=[10,9,38,6,765]
a=np.array(lst)
np.sqrt(a)

a=np.array([1.3,4.5,7,8.9])
print(a.round(0))



a=np.random.randint(1,7,(100,2))
print(a.shape)


b=np.random.randint(1,7,200)
print(b.shape)

d=b.reshape((100,2))
print(d)
print(d.shape[1])

x=np.array([1,2,3,4,5,6,7,8,9])
y=x.reshape((9,1))
y=x.reshape((-1,1))

print(np.sqrt(x))















