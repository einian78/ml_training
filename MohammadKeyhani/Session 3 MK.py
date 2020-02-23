# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 11:31:14 2020

@author: keyha

Playing with libraries and data. You can do the same exercise with the house prices dataset.

"""

import numpy as np #if you don't want to write 'numpy" every time
import pandas as pd #if you don't want to write "pands" every time
#these abbreviations for these two libraries have become standard practice

import os
from sklearn import linear_model as lm
import matplotlib.pyplot as plt

lst=[4,5,6]
print(np.mean(lst))

#change directory to where the data file is
os.chdir(r"C:\Users\keyha\Dropbox\ml_training\Data\diabetes")
df_bk=pd.read_csv('diabetes.csv')
print(df_bk.describe())

