"""
Taylor series/roundoff errors fight each other when deciding how big of a step
size to use when calculating numerical derivatives. If we allow ourselves to 
evaluate our function f at 4 points (x +/- delt; x +/- 2*delt)

a) what should our estimate of the first derivative at x be?
"""

import numpy as np

#let's use the exp function as the function we would like to take the derivative

x=0.0987656
eps=2**-52
dx=eps**(1/5)
dx=0.5*dx

x1=x+dx
x2=x-dx
x3=x+(2*dx)
x4=x-(2*dx)
dx=x1-x

f1=np.exp(0.01*x1)
f2=np.exp(0.01*x2)
f3=np.exp(0.01*x3)
f4=np.exp(0.01*x4)
deriv=(8*(f1-f2)-f3+f4)/(12*dx)
print('derivative is ',deriv,)

"""
b) Now that we have the operator for the derivative, what should delta be in
terms of the machine precision and various properties of the function?
Show for f(x)=exp(x) and f(x)=exp(0.01x) that your estimate of the optimal delt
is at least roughly correct. 
"""
# Delta determined by hand. See pdf.

eps=2**-52
true_func=np.exp(x)
#true_func=np.exp(0.01*x) 
deriv_true_func=np.exp(x)
#deriv_true_func=((0.01)**5)*np.exp(0.01*x)

#Idea is to check id we get the smallest error with our dx value.
err=abs(deriv-deriv_true_func)

print('the error is ',err,)
