
import numpy as np


##################################
# Write a function that combines two lists by alternatingly taking elements,
#  e.g. [a,b,c], [1,2,3] → [a,1,b,2,c,3].
A = ['a','b','c']
B = [1,2,3]
C = A + B
print(C)

D = []
for i in range(len(A)):
    D.append(A.pop(0))
    D.append(B.pop(0))

print('concatenated Series of A and B: ', D)


##################################
# Write a function that computes the list of the first 100 Fibonacci numbers. 
# The first two Fibonacci numbers are 1 and 1. The n+1-st Fibonacci number can
# be computed by adding the n-th and the n-1-th Fibonacci number. The first few are therefore 1, 1, 1+1=2, 1+2=3, 2+3=5, 3+5=8.

F=[]
b=0
a = 1
for i in range(0,100):
    c = a + b
    a = b
    b = c
    F.append(b)

print('Fibonacci list : ', F)


##################################
# calculate a^n
a = int(input('Please Enter a: '))
n = int(input('Please Enter n: '))

print('Usual method a^n: ', a**n)
b=1
for _ in range(n):
    b = b*a

print('Unusual method a^n: ', b)


##################################
# calculate n!
def factorial_func(n):
    x = 1
    for i in range(2,n+1):
        x = x * i
    return x

n=int(input("Please enter n: "))

factn = factorial_func(n)
print("N factorial of ", n, " is: ", factn)