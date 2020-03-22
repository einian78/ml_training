import numpy as np
import math
from scipy import optimize
import matplotlib.pyplot as plt


def pifunc(n):
    #r = (4/(2*n+1)*pow(-1,n))
    r = (4/(2*n-1)*pow(-1,1-n))
    if n == 0:
        r = 0
    elif n == 1:
        #r = 3
        r = 4
    else:
        r = r + pifunc(n-1)
    return(r)


print(pifunc(1000))


def expfunc(x,n):
    r = pow(x,n)/(math.factorial(n))
    if n == 0:
        r = 0
    elif n ==1:
        r = 1
    else:
        r = r + expfunc(x,n-1) 
    return(r)

print(expfunc(2,1000))

E=[]
for x in range(0,10):
    #print(expfunc(x, 1000))
    E.append(expfunc(x, 20))

print(E)

x0=[0]
expsol = optimize.root(expfunc, x0, 10)

x = np.arange(0,10,0.01)
y = expfunc(x,10)

plt.plot(x,y)
plt.show()

