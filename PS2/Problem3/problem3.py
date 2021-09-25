"""
Problem 3
First part -- Write a function that models the log base 2 of x valid from 0.5
to 1 to an accurancy in the region better than 10**-6.
Use truncated Chebyshev polynomial fit. 
"""
import numpy as np
from matplotlib import pyplot as plt
from sklearn.metrics import max_error

n=100
x=np.linspace(0.5,1,n)
y=np.log2(x)

coef=np.polynomial.chebyshev.chebfit(x,y,6)
#6 terms is required to have an accuracy better than 10**-6
leg=np.polynomial.legendre.legfit(x,y,6)

y_test=np.polynomial.chebyshev.chebval(x,coef)
y_leg=np.polynomial.legendre.legval(x,leg)

err= np.abs(y-y_test).mean()

print('error for chebfit is', err)

plt.plot(x,y_test)

def mylog2(x):
  mant1, exp1 = np.frexp(x)
  mant2, exp2 = np.frexp(np.e)


  log_mant1 = np.polynomial.chebyshev.chebval(mant1,coef)
  log_mant2 = np.polynomial.chebyshev.chebval(mant2,coef)

  return (log_mant1 + exp1)/(log_mant2 + exp2)
  #by using the rules of logarithm, the natural log of a positive number can be
  #described by what this function is returning. Thus, it goes through log base
  #2 in order to take the natural log. 

x=np.linspace(0.5,1,n)
mylog2(3)

#Below is for the RMS between Legendre polynomials and Chebyshev

rms_cheb=np.sqrt(np.mean((y_test-y)**2))
rms_leg=np.sqrt(np.mean((y_leg-y)**2))
print('The RMS of Chebyshev is', rms_cheb,'wheras the RMS of Legendre polynomials is', rms_leg)

#maximum error
max_cheb=max_error(y,y_test)
max_leg=max_error(y,y_leg)
print('The max error in Chebyshev is', max_cheb,'wheras the max error of Legendre polynomials is', max_leg)


#On average, the error in Chebyshev is smaller than using Legendre polynomials. 
