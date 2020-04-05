import numpy as np
import pandas as pd

diabetes = pd.read_csv("../../Data/diabetes/diabetes.csv")

colnames = list(diabetes.columns)

a = diabetes[['AGE','SEX']]
a = diabetes[['AGE','SEX']].to_numpy()
a = np.array(diabetes[['AGE','SEX']])
diabetes[:-10]
diabetes[20:-10]
diabetes[::4]
diabetes[['AGE','SEX']][5:10]
diabetes.loc[5:10,['AGE','SEX']]
diabetes[diabetes.AGE>50]


a=np.random.randn(6,4)
df = pd.DataFrame(a)
df = pd.DataFrame(a, columns = ['a1','a2','a3','a4'],index = ['b1','b2','b3','b4','b5','b6'])
df.loc['b2':,['a3','a1']]
df.iloc[3:,]
zOIUYHGFXZBV CX?>,M NBM,./'
7]001  `'