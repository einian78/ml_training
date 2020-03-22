# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import scipy as sp

A = np.array([[2,1,3],[2,6,8],[6,8,18]])
B = np.array([1,3,5])


x= np.linalg.solve(A,B)

A_inv = np.linalg.inv(A)
A_A_inv = A @ A_inv
xx = A_inv @ B

temp1 = np.abs(x) < 1E-5
AA = A.copy()
x [np.abs(x) < 1E-5] = 0

I3 = np.eye(3)
z3 = np.zeros((3,5))


