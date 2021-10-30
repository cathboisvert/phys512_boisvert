"""
Problem 1
--------------
This question requires us to write a function that will
shift an array by an arbitrary amount using convolution.

Function should take 2 arguments:
 1) Array
 2) Amount by which to shift the array

"""

import numpy as np
from scipy import signal
from matplotlib import pyplot as plt


#Inspiration from Jon's shifting example
#and from convolution example
def gauss_shift(array,shift):
    
    #making sure shift is an integer
    shift=int(shift)
    N=np.size(array)
    
    #function to convolve with: delta function
    g=signal.unit_impulse(N,shift)
    
    #convolution
    ft1=np.fft.fft(array)
    ft2=np.fft.fft(g)
    
    return np.real(np.fft.ifft(ft1*ft2))

#Also need to plot gaussian starting at center of array
#shifted by half the array length

x=np.arange(-5,10,0.1)

N=np.size(x)
shift=0.5*np.size(x)
center=x[int(shift)]

y=np.exp(-(x-center)**2/(1.5**2))

y_new=gauss_shift(y,shift)

plt.plot(y)
plt.plot(y_new)

plt.savefig('gauss_shift.png')
