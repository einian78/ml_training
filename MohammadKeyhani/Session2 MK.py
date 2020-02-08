# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 10:41:39 2020

@author: keyha
"""

########## Print

print("Hello World")
print("This is a test")
print("This is Mohammad Keyhani's first python script")

########## Variables
a=10
b=20.0 #the decimal makes it a float

print(a,b)
print('a=', a, 'and b=', b)

########## Inputs

c=input('Please enter a number') #After this line console waits for an input, will save as string
c=int(c)
print(a+c)

d=input('Please enter a number')
d=float(d)
print(b+d)

########## Combining strings

s1=input("Please enter your first name")
s2=input("Please enter your last name")
print('Your fuull name is:', s1+' '+s2)
s3=s1+' '+s2
print(s3)

########## For loop

for i in ['a', a, 12, 3.14, 'b', b]:
    print(i)
    
print(i) #there is no code to end the loop, just remove the tab
    
########## Nested Loop

for i in ['a', a, 12, 3.14, 'b', b]:
    print(i)
    for j in ['a', 'b']:
        print(j)
        
for i in ['a', 'c', '12', '3.14', 'c', 'atalmatal']:
    for j in ['1', '2']:
        print(i+j) 

for i in ['a', 'c', 12, '3.14', 'c', 'atalmatal']:
    for j in ['1', '2']:
        print(str(i)+str(j)) 
        
########## Check the type of a variabe: Either look in variable explorer window or use type command

type(a)

print(a+b) #If you run the type and print commands together, type no longer prints

print(type(a)) #this is how you can force it to print
print(a+b)

########## Ranges

for i in range(10): #starts from 0 and goes to 9
    print(i)
    
for i in range(3, 10): #starts from 3
    print(i)
     
for i in range(6, 10, 3) #6 to 9 in steps of 3
    print(i)
    
########## If command
    
if a<b:
    print("a<b")
else:
    print("a>=b")
    
########## Lists and Append
    
a=[] #define a list
for _ in range(10): #using _ instead of i helps avoid using an extra variable
    s=input("Enter a name: ")
    a.append(s)
print(a)

#More efficient version:
a=[] #define a list
for _ in range(10): #using _ instead of i helps avoid using an extra variable
    a.append(input("Enter a name: "))
print(a)