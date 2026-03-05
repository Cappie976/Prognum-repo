#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np



function = input("your function is: ")
a = float(input("the lower bound is: "))
b = float(input("the higher bound is: "))
N = 100000   

x = np.random.uniform(a,b,N)

func = eval(function)

#monte carlo formula
((b-a)/N) * np.sum(func)
print(y)

