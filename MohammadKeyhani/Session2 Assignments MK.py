# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 11:08:04 2020

@author: keyha
"""

""" Assignment 1: 
    
Write a program to:Input n
Read n numbers, then calculate the average and variance
"""

print("This is Mohammad Keyhani's program to calculate the average and variance of N integers.")
n=int(input("Please enter N: "))

a=[] #define a list
for i in range(n):
    a.append(int(input("Enter integer number " +str(i+1)+ " of " +str(n)+ ": ")))
print("The list of integers entered is: ")
print(a)

#calculate average
sum=0
for i in range(n):
    sum=sum+a[i]
av=sum/n
print("The average of the integers entered is: "+str(av))

#calculate variance
sumofsquares=0
for i in range(n):
    sumofsquares=sumofsquares+(a[i]-av)**2
var=sumofsquares/(n-1)
print("The variance of the integers entered is: "+str(var))


""" Assignment 2:

Read n numbers and sort by descending
Will need to use a list
"""

print("This is Mohammad Keyhani's program to sort a list of N integers.")
n=int(input("Please enter N: "))

b=[] #define a list
for i in range(n):
    b.append(int(input("Enter integer number " +str(i+1)+ " of " +str(n)+ ": ")))
print("The list of integers entered is: ")
print(b)

#Sort using the Bubble Sort algorithm
for i in range(n):
    for j in range(n-i-1):
        if b[j]>b[j+1]:
            b[j], b[j+1] = b[j+1], b[j]

print("The sorted list (using the Bubble Sort algorithm) is: ")
print(b)

""" Assignment 3:

Take two variable inputs, switch their values without using a third variable
Do not use string or lists

"""

print("This is Mohammad Keyhani's program to swap two integers without using a temporary third variable")
num1=int(input("Please enter the first integer: "))
num2=int(input("Please enter the second integer: "))
print(num1, num2)

#the coding method
num1, num2 = num2, num1
print("Swapped using the python coding syntax:")
print(num1, num2)

#the mathematical method
num1=num1+num2
num2=num1-num2
num1=num1-num2
print("Swapped using the mathematical method:")
print(num1, num2)
