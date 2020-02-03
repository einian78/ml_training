# -*- coding: utf-8 -*-
"""
Created on Sun Feb 02 10:35:50 2020

@author: maryam_einian
"""

print("Hello World!")
print('This is the test')
print("This is Maryam's first code")
#print "Maryam"  #only in python 2.7

###########################
a=10
b=20.0
print('a=', a, 'and b=', b)

###########################
c = input('Please enter  number: ')
c = int(c)
print('a+c=', a+c)

###########################
d = input('Please enter  number: ')
d = float(d)
print('a+d=', a+d)

###########################

s1=input("Please enter your first name: ")
s2=input("Please enter your last name: ")

print("Full name is: ", s1 + ' ' + s2)


###########################
# for always reads from a list
for i in ['a', a, 12, 3.14, 'b', b]:
    for j in ['1', '2']:
        print(str(i)+str(j))
        

print(type(a))     

###########################
lst = range(6,10,3)
for i in lst:       #range(10):
    print(i)
    
###########################
if a<b:
    print("a<b")
else:
    print('a>=b')    
    
###########################
A = []
for _ in range(10):
    s=str(input('enter a name: '))
    A.append(s)
print(A)
    
    
    
    
    
   
        