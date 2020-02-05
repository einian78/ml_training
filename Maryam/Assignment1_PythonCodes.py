
###########################################
# 4-	Write a python program to calculate mean and variance of n numbers without using any list.
x=0
s=0
w=0
n=0
    
while x!= -1:
    x = float(input("Please Enter a value: "))
    if x!= -1:    
        w = w+x
        s = s+x*x
        n += 1
    
xbar = w/n
var = (s-w*w/n)/(n-1)

print('counter =', n)
print('mean= ', xbar)
print('var = ', var)


###########################################
#5-	Write a program to swap values of two variable without using third variable (template variable).
a = float(input("Please Enter first number: "))
b = float(input("Please Enter second number: "))

print("a and b prior to swap are: ", a, b)

a = a + b
b = a - (2*b)
a = (a-b)/2
b = a + b

print("a and b after swap are: ", a, b)



###########################################
#6-	Write a python program to sort N numbers descending.
lst= [7,9,8,1,5,3,2,6,4]

for i in range(len(lst)):
    for j in range(i+1, len(lst)): 
        if ( lst[i]> lst[j] ):
            c = lst[i]
            d = lst[j] 
            lst[i] = d
            lst[j] = c


print(lst)
