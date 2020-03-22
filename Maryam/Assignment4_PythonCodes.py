
####################################################
# Expected value for a toss with weighted values And plot the histogram 
#

import numpy as np
import matplotlib.pyplot as plt
A = [1,2,3,4,5,6]
W = [1,2,3,4,5,6]
#W = [1,1,1,1,1,1]

c = 0
d = 0
F = []

for i in range(len(A)):
    c = c + A[i]*W[i]
    d = d + 1
    F.append(A[i]*W[i])

EV = c/d
print("Expected value of a weighted Toss is: ", EV)
print("The weighted list is: ", F)


plt.hist(F,  density=True)
plt.title("Histogram of a weighted Toss")
plt.show()


####################################################
# Central limit theorem for unfair weighted class 
#
import numpy as np
import matplotlib.pyplot as plt
A = [1,2,3,4,5,6]
ev2 = []
c2 = 0
d2 = 0

#wl = A.copy()
for k in range(1,1000):
    F2 = []
    for i in range(len(A)):
        wl=[]              
        for j in range(len(A)):
            w = np.random.randint(1,6)
            wl.append(w)
        
#        wl = np.random.shuffle(A)
        c2 = c2 + A[i]*wl[i]
        d2 = d2 + 1
        F2.append(A[i]*wl[i])
    print(F2)
    ev2.append(c2/d2)

plt.hist(ev2,  density=True)
plt.title("Histogram of a weighted Toss")
plt.show()




####################################################
# Solve a linear equation for 3X3 equation (Matrix Inverse) 
#
import numpy as np

A = [[1,1,1],[0,2,5],[2,5,-1]]
B = [6,-4,27]

a = np.array(A)
b = np.array(B)

x1 = np.linalg.solve(a,b)
print("1st method: numpy solver", x1)

Am = np.linalg.inv(A)
x2 = np.dot(Am,b)
print("2nd method: dot product of inverse matrix: ", x2)


####################################################
#List of point coordinates (x,y)  a=[[10,2],[7,6],[4,5],[3,7]] can make a rectangular 
import numpy as np

al=[[10,2],[7,6],[4,5],[3,7]]
a = np.array(al)


x = 0
y = 0
# finding the central points
for i in range(0,4):
    x = x + a[i,0]
    y = y + a[i,1]

d =[]
# find if the distance between the central point and each coordiante point if the same
for i in range(0,4):
    d.append(np.sqrt(pow(a[i,0]-x/4 , 2) + pow(a[i,1]-y/4, 2))) 

b = np.unique(d)
print(b)

if len(b)==1:
    print("Array may form a rectangular")
else:
    print("Array may not form a rectangular")