# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 2020

@author: keyha
"""

""" Assignment 1: 
    Write a function that combines two lists by alternatingly taking elements, e.g. [a,b,c], [1,2,3] → [a,1,b,2,c,3].
"""
print("")
print("This is Mohammad Keyhani's program to that combines two lists by alternatingly taking elements from each.")
a=input("Please enter the first list: ")
b=input("Please enter the second list: ")
print("")
c=[]

if len(a)==len(b): #the case where the two input lists have equal number of elements
    print("The two lists have equal lengths.")
    for i in range(len(a)):
        c.append(a[i])
        c.append(b[i])
elif len(a)<len(b): #the case where list a has less elements than list b
    print("The second list has more elements than the first list.")
    for i in range(len(a)):
        c.append(a[i])
        c.append(b[i])
    for i in range(len(a), len(b)):
        c.append(b[i])
elif len(a)>len(b): #the case where list b has less elements than list a
    print("The first list has more elements than the second list.")
    for i in range(len(b)):
        c.append(a[i])
        c.append(b[i])
    for i in range(len(b), len(a)):
        c.append(a[i])

print("The combined list is: ")
print(c)  


""" Assignment 2: 
    Write a function that computes the list of the first 100 Fibonacci numbers. The first two Fibonacci numbers are 1 and 1. 
    The n+1-st Fibonacci number can be computed by adding the n-th and the n-1-th Fibonacci number. The first few are therefore 1, 1, 1+1=2, 1+2=3, 2+3=5, 3+5=8.
"""
print("")
print("This is Mohammad Keyhani's program to calculate the first 100 Fibonacci numbers.")
print("")
f=[1,1]

for i in range(2, 100):
    f.append(f[i-2]+f[i-1])

print(f)


""" Assignment 3: 
    Write a program to take two numbers a and n and calculate a to the power of n (n can be negative too)
"""
print("")
print("This is Mohammad Keyhani's program to take two integers a and n and calculate a to the power of n (n can be negative too)")
a=int(input("input the integer a: "))
n=int(input("input the exponent n: "))
print("")

print("using Python's built-in power function, a to the power of n is: ")
print(a**n) # could also use print(pow(a,n))

if n==0:
    ans=1
elif n>0:
    ans=a
    for i in range(n-1):
        ans=ans*a
elif n<0:
    ans=a
    for i in range(abs(n)-1):
        ans=ans*a
    ans=1/ans

print("")
print("using my code, a to the power of n is: ")
print(ans)


""" Assignment 4: 
    Write a program to take an integer n and calculate n! (the factorial function).
"""
import math
print("")
print("This is Mohammad Keyhani's program to take an integer n and calculate n! (the factorial function).")
n=int(input("input a positive integer n: "))
print("")

print("using Python's built-in math.factorial() function, n! is: ")
print(math.factorial(n))

ans=1
for i in range(1,n+1):
        ans=ans*i
        
print("")
print("using my code, n! is: ")
print(ans)
