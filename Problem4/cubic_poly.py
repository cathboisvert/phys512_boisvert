"""
Problem 4 - rational function interpolation
"""
import numpy as np
from matplotlib import pyplot as plt
import math

xmax=math.pi/2
xmin=-math.pi/2

def rat_eval(p,q,x):
    top=0
    for i in range(len(p)):
        top=top+p[i]*x**i
    bot=1
    for i in range(len(q)):
        bot=bot+q[i]*x**(i+1)
    return top/bot

def rat_fit(x,y,n,m):
    assert(len(x)==n+m-1)
    assert(len(y)==len(x))
    mat=np.zeros([n+m-1,n+m-1])
    for i in range(n):
        mat[:,i]=x**i
    for i in range(1,m):
        mat[:,i-1+n]=-y*x**i
    pars=np.dot(np.linalg.inv(mat),y)
    p=pars[:n]
    q=pars[n:]
    print(p,q)
    return p,q


#1*p0 + x*p1 +x**2+p2+... -q1*x - q2*x**2... = y

n=4
m=5
x=np.linspace(xmin,xmax,n+m-1)
y=np.cos(x)
#y=1/(1+(x**2))
p,q=rat_fit(x,y,n,m)
xx=np.linspace(x[0],x[-1],1001)
y_true=np.cos(xx)
#y_true=1/(1+(xx**2))
pred=rat_eval(p,q,xx)
plt.clf();plt.plot(x,y,'*')
plt.plot(xx,y_true)
plt.plot(xx,pred)

fitp=np.polyfit(x,y,n+m-1)
pred_poly=np.polyval(fitp,xx)

plt.clf();plt.plot(x,y,'*');plt.plot(xx,y_true);plt.plot(xx,pred)
