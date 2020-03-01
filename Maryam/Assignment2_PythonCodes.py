
###########################################
# Assignment 1:	
# Read a number create smallest and largest numbers with similar digits
import numpy as np

a = int(input("Please Enter a number: "))

def split_number(n):
    nn = 0
    NS = []
    while n/10 >= 0.1:
        nn = nn + 1
        m = int(n%10)
        n = int(n/10)
        NS = np.append(NS, m)

    return NS


Ap = split_number(a)
print("Ap after spliting a: ", Ap)

c= 0
for i in range(0, len(Ap)):
    for j in range(i+1, len(Ap)): 
        if ( Ap[i]> Ap[j]):
            c = Ap[i]
            d = Ap[j] 
            Ap[i] = d
            Ap[j] = c
          


print("Ap after sorting number: ", Ap)

# calculating the largest number 
b=0
i=0
for i in range(0, len(Ap)):
    b = b + Ap[i]*(10**i)


# calculating the smallest number by moving the zeros to digits other than first
for i in range(0, len(Ap)):
    if (Ap[0]==0 and Ap[i]!=0):
        c = Ap[0]
        d = Ap[i]             
        Ap[0] = d
        Ap[i] = c  

c=0
i=0
for i in range(0, len(Ap)):
    c = c + Ap[i]*(10**(len(Ap)-i))

print("Largest number derived from number a is: ", b)
print("Smallest number derived from number a is: ", c)

###########################################
# Assignment 2:
# Expected value for a toss with weighted values

lst = [1,2,3,4,5,6]
wt = [6,5,4,3,2,1]
expv = 0
tot = 0
tow = 0

for i in range(0, len(lst)):
    tot = tot + lst[i]*lst[i]
    tow = tow + lst[i]*wt[i]

expv = tot/len(lst)
expw = tow/len(lst)
print('Expected value of tossed with with weighted values are: ', expv, expw)

