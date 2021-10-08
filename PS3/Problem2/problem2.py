"""
Problem 2. a)
The goal is to write a program that solves for the decay products of U238. 
Can use the ODE solver from scipy. 
Make sure to include all decay products in the chain

Half-life of U238: 4468 billion years
"""

import numpy as np
from scipy import integrate
import time
from matplotlib import pyplot as plt

min=60
hour=60*min
day=24*hour
week=7*day
month=4.34524*week
year=12*month

chain=np.array([4.468e9*year, 24.1*day, 6.7*hour, 2.455e5*year, 7.5380e4*year, 1600*year, 3.8235*day, 3.10*min, 26.8*min, 19.9*min, 1.643e-4, 22.3*year, 5015*year, 138376*day])

def fun(x,y):
    chain=np.array([4.468e9*year, 24.1*day, 6.7*hour, 2.455e5*year, 7.5380e4*year, 1600*year, 3.8235*day, 3.10*min, 26.8*min, 19.9*min, 1.643e-4, 22.3*year, 5015*year, 138376*day])
    dydx=np.zeros(15)
    for i in range(15):
        if i==0:
            dydx[i]=-y[i]*np.log(2)/chain[i]
        elif i!=0 and i!=14:
            dydx[i]=y[i-1]*np.log(2)/chain[i-1]-y[i]*np.log(2)/chain[i]        
        else:
            dydx[i]=y[i-1]*np.log(2)/chain[i-1]
       
    return dydx


y0=np.zeros(15) #length of chain including stable lead
y0[0]=1
x0=0
x1=chain[0]*1

ans_stiff=integrate.solve_ivp(fun,[x0,x1],y0,method='Radau')


#print(ans_stiff.y[3,:]/ans_stiff.y[4,:])
#print(ans_stiff.y[0,:]/ans_stiff.y[14,:])
#plt.plot(ans_stiff.t[0:22],ans_stiff.y[4,0:22]/ans_stiff.y[3,0:22])
#plt.plot(ans_stiff.t[0:4],ans_stiff.y[14,0:4]/ans_stiff.y[0,0:4])
#plt.plot(ans_stiff.t,ans_stiff.y[14,:]/ans_stiff.y[0,:])
#print(ans_stiff.y[14,:]/ans_stiff.y[0,:])

# analytical solution to the ratio of Pb206/U238
analytical=((1-np.exp(-np.log(2)*ans_stiff.t/chain[0]))/np.exp(-np.log(2)*ans_stiff.t/chain[0]))
#test=1/(np.exp((-chain[0])*ans_stiff.t))-1
print('The error is',np.std(analytical-(ans_stiff.y[14,:]/ans_stiff.y[0,:])))
