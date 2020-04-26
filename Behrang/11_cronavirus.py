# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 10:00:09 2020

@author: koushb
"""

#https://covid19stats.alberta.ca/
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit#,root,fsolve
import matplotlib.dates as mdates
from sklearn.metrics import mean_squared_error as mse

df=pd.read_csv('..\Data\covid19dataexport.csv',index_col=0)
df["Date reported"]=pd.to_datetime(df['Date reported'])
basedate=pd.Timestamp("2020-03-1")
df['time since']=(df['Date reported']-basedate).dt.days

table1=pd.pivot_table(df,values='Gender',index=['Date reported','time since'],aggfunc=np.size)
table1['cumsum']=table1['Gender'].cumsum()
table1.reset_index(inplace=True)
table1.drop('Gender',axis=1,inplace=True)


x=table1['time since']
y=table1['cumsum']

def myfunc(x,a,b,c):
    r=c/(1+np.exp(-(x-b)/a))
    return(r)

#xx=np.arange(90)
#a=20
#b=40
#c=2500
#yy=myfunc(xx,a,b,c)

fit=curve_fit(myfunc,x,y,p0=[20,40,2500])
a,b,c=fit[0]
c=int(c)-1
ndays=120

xx=np.arange(ndays)
yy=myfunc(xx,a,b,c)
plt.plot(table1['time since'],table1['cumsum'],'.')
plt.plot(xx,yy)
plt.show()

y_pred=myfunc(x,a,b,c)
err=np.sqrt(mse(y,y_pred))


for sol in range(ndays):
    r=int(c)-myfunc(sol,a,b,c)
    if r<1:
        break

#sol = int(fsolve(lambda x : myfunc(x,a,b,c) - c,b))
#def myfunc2(x):
#    r=c/(1+np.exp(-(x-b)/a))-int(c)
#    return(r)
#root(myfunc2,10,tol=10)
#sol=int(fsolve(myfunc2,10))
endday=basedate+pd.DateOffset(days=sol)

print('Predicted total number of infected cases:',int(c))
print('Predicted infection end date:',endday.strftime("%d %B %Y"))

r=[]
for i in range(ndays):
    r.append(basedate+pd.DateOffset(days=i))



a_r=np.array([r,yy]).T
df_pred=pd.DataFrame(a_r,columns=['Date reported','prediction'])


df_total=pd.merge(df_pred,table1,on='Date reported',how='left')


fig,ax=plt.subplots(1)
ax.plot(df_total['Date reported'],df_total['prediction'],c='r')
ax.scatter(df_total['Date reported'],df_total['cumsum'],s=2,c='b')
locator = mdates.AutoDateLocator()
formatter = mdates.ConciseDateFormatter(locator)
ax.xaxis.set_major_locator(locator)
ax.xaxis.set_major_formatter(formatter)
plt.ylabel('Total number of cases')
plt.title('Alberta Crona Virus cases. error:'+str(np.round(err,3)))
plt.show()











