# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 18:06:28 2020

@author: koushb
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv("../Data/diabetes/diabetes.csv")
#plt.hist(df.target)

df.hist('target')
plt.show()

df['target cat']=pd.cut(df.target,bins=[0,100,150,1000],labels=[0,1,2])
df['target cat'].hist()
plt.show()

sns.pairplot(df,vars=['AGE','BMI','S1'],hue='target cat')


cmap = sns.cubehelix_palette(as_cmap=True, dark=0, light=1, reverse=True)
sns.kdeplot(df['BMI'],df['target'],cmap=cmap)


g = sns.jointplot(x="BMI", y="target", data=df, kind="kde", color="m")
g.plot_joint(plt.scatter, c="w", s=30, linewidth=1, marker="+")
g.ax_joint.collections[0].set_alpha(0)
g.set_axis_labels("$X$", "$Y$");
plt.show()
