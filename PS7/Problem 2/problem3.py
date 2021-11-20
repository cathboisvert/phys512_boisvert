"""
Problem 3
---------------------------
The goal of this problem is to repeat the previous problem 
but a ratio-of-uniforms generator. 

This code is inspired by Rigel's tutorial.
"""
import numpy as np
from matplotlib import pyplot as plt

N=1000000
gamma = 1

#Generate exponential distribution
def exp_pdf(x,gamma):
    return np.exp(-x*gamma)

x=np.linspace(0,0.5e3,N)
u=np.sqrt(exp_pdf(x,gamma))
v=x*u

#calculating bounds
u_min=np.min(u)
u_max=np.max(u)
v_min=np.min(u)
v_max=np.max(u)

#Generate the random numbers
u=np.random.uniform(low=u_min,high=u_max,size=N)
v=np.random.uniform(low=v_min,high=v_max,size=N)
#Do the rejection Step
keep = u < np.sqrt(exp_pdf(v/u,gamma)) 
rand_exp = v[keep]/u[keep]

#Plot Results
plt.plot()
plt.hist(rand_exp[np.abs(rand_exp)<100],bins=1000,density=True)
xs = np.linspace(0,10,1000)
plt.plot(xs,exp_pdf(xs,gamma), label='analytical')
plt.xlim(min(xs),max(xs))
plt.legend()

print(len(rand_exp)/(len(u)) * 100,"% Efficient")
