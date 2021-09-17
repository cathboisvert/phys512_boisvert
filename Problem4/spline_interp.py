"""
Problem 4 - spline interpolation
"""

import numpy as np
from scipy import interpolate
from matplotlib import pyplot as plt
import math


#xmin=-math.pi/2
xmin=-1
#xmax=math.pi/2
xmax=1
npt=100
# Observation: the more points I have, the more the error decreases. 
x=np.linspace(xmin,xmax,npt)
#y=np.cos(x)
y=1/(1+(x**2))
xx=np.linspace(x[0],x[-1],2001)

spln=interpolate.splrep(x,y)
yy=interpolate.splev(xx,spln)

plt.clf()
plt.plot(x,y,'*')
plt.plot(xx,yy)
plt.plot(xx,1/(1+(xx**2)))
plt.show()

rng = np.random.default_rng(seed=12345)
N_resamples = 10
N_samples = 80
errors = []
for i in range(N_resamples):
  #Making a list of all the indices
  indices = list(range(x.size))
  #Choosing N_samples indices values to use for new interpolation
  to_interp = rng.choice(indices,size=N_samples, replace=False)
  to_interp.sort() #Making sure that x is increasing
  #Taking the other indices to keep checking for error
  to_check = [i for i in indices if not (i in to_interp)]
  #Using new interpolation points to interpolate
  new_interpolation = interpolate.CubicSpline(x[to_interp],y[to_interp])
  #Generate y values to check order
  interpolated_y = new_interpolation(x[to_check])
  real_y = y[to_check]
  #Calculating absolute value of differences
  errors.append(np.abs(interpolated_y - real_y))

#Processing statistics
error=np.mean(errors)
error_std=np.std(errors)

print(f"The error is {error:.10f} +/- {error_std:.10f}")
