"""
e)
advection code to use downwind/Lax scheme
assume critical value of alpha to be 0.5
"""
import numpy as np
from matplotlib import pyplot as plt
import time

#Insparation from Jon's advection code

#starting with a boxcar
if True: #do a boxcar
    rho=numpy.zeros(n)
    rho[n//3:(2*n//3)]=1
    x=numpy.arange(n)*dx
else:
    x=numpy.arange(n);x=x-0.5*n
    rho=numpy.exp(-0.5*(x/20)**2)

plt.ion()
plt.clf()
plt.axis([0,n,0,1.1])
plt.plot(x,rho)
plt.draw()

dt=1.0
for step in range(0,150):
    #time.sleep(0.2)
    plt.pause(0.05)
    #take the difference in densities
    drho=rho[1:]-rho[0:-1]
    #update density.  We haven't said what happens at
    #cell 0 (since cell -1 doesn't exist), ignore for now
    rho[1:]=rho[1:]-v*dt/dx*drho
    rho[0]=rho[-1] #periodic
    plt.clf()
    plt.axis([0,n,0,1.1])
    plt.plot(x,rho)
    plt.pause(0.001)
    #plt.draw()
