"""
Taylor series/roundoff errors fight each other when deciding how big of a step
size to use when calculating numerical derivatives. If we allow ourselves to 
evaluate our function f at 4 points (x +/- delt; x +/- 2*delt)

a) what should our estimate of the first derivative at x be?
"""

import numpy as np

#let's use the sine function as the function we would like to take the derivative

x=42
eps=2**-52
dx=eps**(1/5)

x1=x+dx
x2=x-dx
x3=x+(2*dx)
x4=x-(2*dx)
dx=x1-x

f1=np.exp(x1)
f2=np.exp(x2)
f3=np.exp(x3)
f4=np.exp(x4)
deriv=(8*(f1-f2)-f3+f4)/(12*dx) #derivative not working
print('derivative is ',deriv,)

#f0=np.exp(x-dx)
#deriv=(f2-f0)/(2*dx)
#print('derivative is ',deriv,)
