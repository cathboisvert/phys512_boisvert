"""
Problem 1
The goal is to plot the electric field from a spherical shell as a function of 
distance from the center of the sphere. 
Make sure the range of the plot covers the z < R and z > R
Make sure one of the z values is R

Basically I want to make a plot of electric field vs z. 
"""

import numpy as np
from scipy import integrate
from matplotlib import pyplot as plt

sig=2.65*10**-5
r=1
eps=8.85*10**-12

N=1001

z_values = np.linspace(1.01,2,1001)

#Below is the function that I would like to integrate. 
#Actually, need to do the substitutions before using the integrator. 

def fun(u):
  return (z-r*u) / (r**2+z**2-2*r*z*u)**1.5

#limits
a=-1
b=1

dx=(b-a)/N

#answers
e_field_quad=[]
e_field_simp=[]
x=[]

#scipy.integrate.quad
for i in range(len(z_values)):
  z=z_values[i]
  #quad integration
  tot=integrate.quad(fun,a,b)
  e_field_quad.append(tot[0])
  #simpson integration
  x_simp=np.linspace(a,b,N)
  y_simp=fun(x_simp)
  S = dx/3 * (y_simp[0]+y_simp[-1]+4*np.sum(y_simp[1::2])+2*np.sum(y_simp[2:-1:2]))
  e_field_simp.append(S)

  x.append(z_values[i])


plt.clf()
plt.plot(x,e_field_quad)
plt.plot(x,e_field_simp)
