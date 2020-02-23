# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 11:08:04 2020

@author: keyha
"""

""" Assignment: 
    
Take a (large) number, and find the smallest and largest numbers that can be produced with the digits of that number. 
All digits have to be used exactly once. Cannot have leading zeroes if the number contains 0 digits.
"""
print("")
print("This is Mohammad Keyhani's program to calculate the smallest and largest numbers that can be produced with the digits of a number.")
n=int(input("Please enter a positive integer: "))

digitlist = [int(x) for x in str(n)] #convert the input number to a list

#Find the largest number
digitlist.sort(reverse=True)
largestnumber = int("".join(map(str,digitlist)))
print("The largest number is: " + str(largestnumber))

#Find the smallest number
digitlist.sort()
if (digitlist[0] == 0): #dealing with the case of leading zeros
    i = digitlist.index(next(filter(None, digitlist))) #find the index of the first non-zero
    digitlist[0], digitlist[i] = digitlist[i], digitlist[0]

smallestnumber = int("".join(map(str,digitlist)))
print("The smallest number is: " + str(smallestnumber))

#altenrative to finding first non-zero: next((i for i, x in enumerate(digitlist) if x), None)
#I'm not happy with either of these methods because they continue searching for nonzeros even after they have found the first one


