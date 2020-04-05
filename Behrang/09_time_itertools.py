# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 09:56:08 2020

@author: koushb
"""
from time import sleep
from tqdm import tqdm

a=0
for i in tqdm(range(10)):
    a=a+i
    sleep(1)



#https://docs.python.org/2/library/itertools.html
import itertools as it

j=0
for i in it.cycle('ABCD'):
    print(i)
    j=j+1
    if j>100:
        break
    

for i in it.chain('behrang','koushavand'):
    print(i)
    
list(it.permutations('ABCD'))

list(it.product('ABCD',repeat=3))

list(it.combinations("ABCD",2))


