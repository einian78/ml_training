# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 18:02:47 2020

@author: koushb
"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, ConstantKernel as C

X=np.array([0,10,20,]).reshape(-1,1)
y=np.array([10,25,20])



#kernel = C(1.0, (1e-3, 1e3)) * RBF(10, (1e-2, 1e2))
kernel=13.9**2 * RBF(length_scale=17.1)
gp=GaussianProcessRegressor(kernel)
gp.fit(X,y)
print(gp.kernel_)

N_X=np.linspace(0,20,1000)
pred,sigma=gp.predict(N_X.reshape(-1,1), return_std=True)

plt.scatter(X, y,label='Observations')
plt.ylim(5,35)
plt.plot(N_X,pred,label='Prediction')
plt.fill_between(N_X, pred-1.96*sigma,pred+1.96*sigma,label='95% confidence interval')
plt.legend(loc='upper left')
plt.show()



#kernel = C(1.0, (1e-3, 1e3)) * RBF(10, (1e-2, 1e2))
kernel=13.9**2 * RBF(length_scale=17.1)
gp=GaussianProcessRegressor(kernel,alpha=0.2)
gp.fit(X,y)
print(gp.kernel_)

N_X=np.linspace(0,20,1000)
pred,sigma=gp.predict(N_X.reshape(-1,1), return_std=True)

plt.scatter(X, y,label='Observations')
plt.ylim(5,35)
plt.plot(N_X,pred,label='Prediction')
plt.fill_between(N_X, pred-1.96*sigma,pred+1.96*sigma,label='95% confidence interval',alpha=0.6)
plt.legend(loc='upper left')


