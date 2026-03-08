#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#creating an executable script


import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
import math

#definition of Gaussian function
def gaussarea(x, A, x0, sigma, z0):
    return A*np.exp(-(x-x0)**2/(2*sigma**2))+z0

#set calling environment
A = float(input('input your amplitude: '))
x0 = float(input('input your value for peak x-value: '))
sigma = float(input('input your value for the peak width: '))
z0 = float(input('input your value for the offset: '))
lower_bound = float(input('ínput the lower bound of the integration: '))
upper_bound = float(input('input the upper bound of the integration: '))

#calculate area
area, error = integrate.quad(gaussarea,lower_bound,upper_bound,args=(A,x0,sigma,z0))

#plot
x = np.linspace(lower_bound-5*sigma,upper_bound+5*sigma,200)
y = gaussarea(x, A, x0, sigma, z0)
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Gaussian area')


#mark area
x_area = np.linspace(lower_bound,upper_bound,200)
y_area = gaussarea(x_area,A,x0,sigma,z0)
plt.fill_between(x_area,y_area, label=f"the area is: {area}")
plt.legend()
plt.show()

