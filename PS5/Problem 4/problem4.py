"""
Problem 4
--------------
This question requires us to write a routine to take the
convolution of two arrays without any danger of wrapping
around.
Perhaps we can add zeros to the end of the input arrays. 
"""
import numpy as np
from matplotlib import pyplot as plt

#Essentially I want to do what I did in q1
#But in a way where the shifted gaussian 
#doesn't come to the beginning of the array.

def conv_safe(f,shift):
    #making sure shift is an integer
    shift=int(shift)
    N=np.size(f)
    #N_new=(1+(1/shift))*N
    N_new=N+2*shift
    N_new=int(N_new)

    new_f=np.pad(f,(0,N_new-N),'constant')
    
    #function to convolve with: delta function
    g=signal.unit_impulse(N,shift)
    new_g=np.pad(g,(0,N_new-N),'constant')
    
    #convolution
    ft1=np.fft.fft(new_f)
    ft2=np.fft.fft(new_g)
    
    nowrap=np.real(np.fft.ifft(ft1*ft2))
    
    return nowrap

x=np.arange(-5,10,0.1)

N=np.size(x)
shift=0.5*np.size(x)
center=x[int(shift)]

y=np.exp(-(x-center)**2/(1.5**2))

y_new=conv_safe(y,0.7*N)
y_new2=conv_safe(y,0.5*N)
y_new3=conv_safe(y,0.9*N)

print(len(y))
print(len(y_new))
print(len(y_new2))
print(len(y_new3))

plt.plot(y,label='function')
plt.plot(y_new,label='0.7')
plt.plot(y_new2,label='0.5')
plt.plot(y_new3,label='0.9')

plt.legend()
