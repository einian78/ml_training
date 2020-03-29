# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 11:04:08 2020

@author: koushb
"""

import numpy as np
import pandas as pd

diabetes=pd.read_csv("../Data/diabetes/diabetes.csv")

colnames=list(diabetes.columns)

a=diabetes[['AGE','BMI']].values
a=diabetes[['AGE','BMI']].to_numpy()
a=np.array(diabetes[['AGE','BMI']])

a=diabetes[0:5]
b=diabetes[  : -10 ]
c=diabetes[ 20 : -10 ]

d=diabetes[::4]

diabetes['AGE'][5:10]

diabetes.loc[5:10,['AGE','S1']]

diabetes[diabetes.AGE>50]





a=np.random.randn(6, 4)
df=pd.DataFrame(a,columns=['a1','a2','a3','a4'],index=['1','100','test',4,'behrang','red'])
df.loc['test':,['a1','a2']]
df.iloc[3:,]








