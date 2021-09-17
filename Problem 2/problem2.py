""" Problem 2
Write a numerical differentiatior. 
If full=false, ndiff should return the numerical derivative, dx, and an estimate
of the error of the derivative. 
If True, then function should return the derivative, dx, and an estimate of the 
error.

"""
#fun is a function, x is a value
import numpy as np

def ndiff(fun,x,full):
  eps=2**-52
  dx=eps**(1/3)

  x1=x+dx
  x2=x-dx

  f1=fun(x1)
  f2=fun(x2)

  deriv=(f1-f2)/(2*dx)

  if full==True:
    print ('The derivative is ',deriv,' with error ',eps,'and optimal dx of',dx,)
  if full==False:
    print ('The derivative is ',deriv,)

ndiff(np.exp,53,True)
