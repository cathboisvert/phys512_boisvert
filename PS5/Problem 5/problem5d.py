"""
Problem 5.d)
----------------
This question requires us to multiply input data
by a window function.
This will drop the spectral leakage of a non-integer
sine wave. 
"""

window=0.5*(1-np.cos(2*np.pi*x/N))
new_f=f*window

plt.plot(np.abs(np.fft.fft(new_f)))
plt.plot(np.abs(f_dft))

#now I want to show at a specific peak 
plt.xlim(0,60)
