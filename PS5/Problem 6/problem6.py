"""
Problem 6 b)
--------------
This problem requires us to generate a random walk.
Must also plot power spectrum
"""
import numpy as np
from matplotlib import pyplot as plt

n=1000

#generating random walk
y=np.cumsum(np.random.randn(n))

#defining the power spectrum
power_spect=np.abs(np.fft.rfft(y))

fun = lambda x,m,b: m*x**b
x=np.linspace(1,len(power_spect),len(power_spect))

logx=np.log10(x)
logy=np.log10(power_spect)

#finding the right parameters with 
m,b=np.polyfit(logx,logy,1)
print('slope is ',m,'with intercept',b)

plt.plot(logx,logy)
plt.plot(logx,m*logx+b)
