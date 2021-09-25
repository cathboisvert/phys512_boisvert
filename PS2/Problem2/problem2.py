"""
Problem 2
"""

import numpy as np
def lorentz(x):
    return 1/(1+x**2)

#my adapative integrator below
def integrate_adaptive(fun,a,b,tol,extra=None):
    #hardwire to use simpsons

    if extra == None:
      x=np.linspace(a,b,5)
      y=fun(x)
      dx=(b-a)/(len(x)-1)
      area1=2*dx*(y[0]+4*y[2]+y[4])/3 #coarse step
      area2=dx*(y[0]+4*y[1]+2*y[2]+4*y[3]+y[4])/3 #finer step
      err=np.abs(area1-area2)
      if err<tol:
        return area2
      else:
        xmid=(a+b)/2
        left=integrate_adaptive(fun,a,xmid,tol/2,extra=[y[0],y[1],y[2],dx])
        right=integrate_adaptive(fun,xmid,b,tol/2,extra=[y[2],y[3],y[4],dx])
        return left+right
    
    else:
      count1 += 2
      x=np.array([a+0.5*(extra[3]),b-0.5*extra[3]])
      y=fun(x)
      dx=extra[3]/2
      area1=2*dx*(extra[0]+4*extra[1]+extra[2])/3
      area2=dx*(extra[0]+4*y[0]+2*extra[1]+4*y[1]+extra[2])/3

      err=np.abs(area1-area2)

      if err<tol:
        return area2
      else:
        xmid=(a+b)/2
        left=integrate_adaptive(fun,a,xmid,tol/2,extra=[extra[0],y[0],extra[1],dx])
        right=integrate_adaptive(fun,xmid,b,tol/2,extra=[extra[1],y[1],extra[2],dx])
        return left+right


#Below is the integrator function done in class.
def integrate_adaptive_class(fun,x0,x1,tol):
  print('integrating between ',x0,x1)
  #hardwire to use simpsons
  x=np.linspace(x0,x1,5)
  y=fun(x)
  dx=(x1-x0)/(len(x)-1)
  area1=2*dx*(y[0]+4*y[2]+y[4])/3 #coarse step
  area2=dx*(y[0]+4*y[1]+2*y[2]+4*y[3]+y[4])/3 #finer step
  err=np.abs(area1-area2)
  if err<tol:
    return area2
  else:
    count1+=2
    xmid=(x0+x1)/2
    left=integrate_adaptive(fun,x0,xmid,tol/2)
    right=integrate_adaptive(fun,xmid,x1,tol/2)
    return left+right


#count1 and count2 are to track how many function calls are required for both
#my own adapative integrator and the one done in class, respectively. 
count1=0
count2=0

integrate_adaptive(np.exp,-10,10,1e-7,None)
integrate_adaptive_class(np.exp,-5,5,1e-7)

#print(count1,count2)

""" For some reason my counters were not working, so I couldn't numerically show
how many function calls I save. However, knowing that I only need to evaluate
the function at 2 points instead of 5, I speculate that the number of function 
calls for my function is approximately 2/5 of the number of function calls made
with the code written in class. """
