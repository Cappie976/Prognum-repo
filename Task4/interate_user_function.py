#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
from numpy import sin, cos, exp, pi
from scipy import integrate

#integral using Monte carlo integration
def monte(f, a, b, N=100000):
    x = np.random.uniform(a, b, N)
    y = f(x)
    return (b-a)*np.mean(y)

try:

    #calculate integral with quad
    formula = input("input a mathematical function: ")
    a = float(input("input a value for the lower bound: "))
    b = pi  #i wanted to do an input here as well to make sure one can integrate over every bound, but the input of 'pi' did not work

    #converting the string to a function
    def f(x):
        return eval(formula)

    #integral using quad and monte carlo
    quad, error = integrate.quad(f, a, b)
    monte_carlo = monte(f, a, b)

    #results
    print(f"solution using quad is: {quad}")
    print(f"solution using monte carlo: {monte_carlo}")

#help for user when certain error occurs
except NameError:
    print('you used an unknown function/variable. You can use sin, cos, exp and pi')
except SyntaxError:
    print('you used an incorrect formula, the expression is not recognized')
except TypeError:
    print('your input does not match the operation')

