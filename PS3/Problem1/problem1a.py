"""
Problem 1
This questions requires us to write a Runga-Kutta order 4 integrator for the
following equation:
dx/dy = y/1-x**2
From x=-20 to x=20, with y(-20)=1
200 steps required. 
"""

import numpy as np
from matplotlib import pyplot as plt

def func(x,y):
  dydx=y/(1+x**2)
  return dydx

#rk4 works
def rk4_step(fun,x,y,h):
  k1=fun(x,y)*h
  k2=h*fun(x+h/2,y+k1/2)
  k3=h*fun(x+h/2,y+k2/2)
  k4=h*fun(x+h,y+k3)
  dy=(k1+2*k2+2*k3+k4)/6 

  return y+dy

y_init=1
x=np.linspace(-20,20,201)
h=np.median(np.diff(x)) # step size 
y=np.zeros(len(x))
y[0]=y_init

for i in range(len(x)-1):
  y[i+1]=rk4_step(func,x[i],y[i],h)

truth=4.57605801504*np.exp(np.arctan(x))
rk4_step(func,x,y,h)

plt.plot(x,y,'*')
plt.plot(x,truth)

print(np.std(truth-y))
