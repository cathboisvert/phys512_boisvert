"""
Problem 2: Exponential Deviates
--------------------------------------
The purpose of this problem is to generate exponential deviates
from another distribution. 

This code is inspired by Rigel's tutorial. 
"""

import numpy as np
from matplotlib import pyplot as plt

#Generate Lorentzian random numbers
def randl(n):
    q=np.pi*(np.random.rand(n)-0.5)
    return np.tan(q)

#Generate Lorentzian distribution
def l_pdf(x,gamma=1):
    return 1/(gamma*np.pi) * 1/(1+np.power(x/gamma,2))

#Generate exponential distribution
def exp_pdf(x,gamma=1):
    return np.exp(-x*gamma)

n=1000000 #number of RNs
ys=randl(n) #generating the Lorentzian RNs
us=np.random.rand(n) #generating uniformely distributed RNs

#Need to scale Lorentzian to make sure that it is greater
#than exponential. 
M=1.7
#Gaussian probability distribution evaluated at y
fs=g_pdf(ys)
#Lorentzian probability distribution evaluated at y
gs=l_pdf(ys)

#Rejection step
keep=us<fs/(M*gs)
exp_rand=ys[keep]

efficiency=len(exp_rand)/len(ys) *100

print(efficiency,"%")

plt.figure()
x=np.linspace(-10,10,1000)
plt.hist(ys,bins=5,density=True)
plt.plot(x,g_pdf(x),label='exponent')
plt.plot(x,M*l_pdf(x),label='lorentz')
plt.legend()
plt.xlim(-10,10)

plt.figure()
plt.hist(exp_rand,bins=30,density=True,label='Samples')
x=np.linspace(min(exp_rand),max(exp_rand),1000)
plt.plot(x,g_pdf(x),label='expected')
plt.legend()
