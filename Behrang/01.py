# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 10:33:30 2020

@author: koushb
"""

print("Hello World")
print('This is a test')
print("This is Behrang's first code")

###################################################
a=10
b=20.0

print('a=',a,'and b=',b)

###################################################

c=input('Please enter a number')
c=int(c)
print(a+c)

#####################################################
d=input('Please enter a number')
d=float(d)
print(b+d)
#####################################################

s1=input("please enter your first name")
s2=input("please enter your second name")

print('Your full name is:',s1+' '+s2)

#####################################################

st="test1"+      ' ' +"test2"
print(st)
#####################################################

for i in ['a','c',12,'3.14','c','atalmatal']:
    for j in ['1','2']:
        print(str(i)+str(j))

#####################################################

print(type(a))
print(a+b)

#####################################################
abc=range(6,10,3)
for i in abc:
    print(i)
#####################################################
if a<b:
    print("a<b")
else:
    print('a>=b')
#####################################################
a=[]
for _ in range(10):
    s=input('enter a name')
    a.append(s)
print(a)

#####################################################
a=[]
for _ in range(10):
    a.append(input('enter a name'))
print(a)






