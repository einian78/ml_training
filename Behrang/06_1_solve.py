# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 09:53:56 2020

@author: koushb
"""

import numpy as np


A=np.array([[2,1,3],[2,6,8],[6,8,18]])
b=np.array([1,3,5])

x = np.linalg.solve(A, b)


A_inv=np.linalg.inv(A)
#A_A_inv=A_inv @ A
xx=A_inv @ b




AA=A.copy()
AA[AA>10]=-8

x[np.abs(x)<.0001]=0


I10=np.eye(10)
z10=np.zeros((10,2))

