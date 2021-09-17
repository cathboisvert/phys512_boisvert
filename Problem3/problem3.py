"""
Problem 3
Write a routine that will take an arbitrary voltage and interpolate to return a temperature

I am choosing to use cubic spline for my interpolation
"""

import numpy as np
from matplotlib import pyplot as plt
from scipy import interpolate
import random

#open("/content/lakeshore.txt")

dat=np.loadtxt("lakeshore.txt") #this puts the entire data into an array

#should now write code to take a random voltage in range of data
V = np.random.uniform(0,1.7)
data = dat


def lakeshore(V,data):
  temp = data[:,0]
  volt = data[:,1]
  #must reverse order of list for interpolation to work
  temp = temp[::-1]
  volt = volt[::-1]

  xx=V

  spln=interpolate.splrep(volt,temp)
  yy=interpolate.splev(xx,spln)

  plt.clf()
  plt.plot(volt,temp,'.')
  plt.plot(xx,yy)

  print('For a voltage of ',xx,' the temperature is ',yy,)

  #now I need to define the error in my answer - bootstrap sampling?
  
  rng = np.random.default_rng(seed=12345)
  N_resamples = 10
  N_samples = 100
  errors = []
  for i in range(N_resamples):
    #Making a list of all the indices
    indices = list(range(volt.size))
    #Choosing N_samples indices values to use for new interpolation
    to_interp = rng.choice(indices,size=N_samples, replace=False)
    to_interp.sort() #Making sure that volt is increasing
    #Taking the other indices to keep checking for error
    to_check = [i for i in indices if not (i in to_interp)]
    #Using new interpolation points to interpolate
    new_interpolation = interpolate.CubicSpline(volt[to_interp],temp[to_interp])
    #Generate y values to check order
    interpolated_temp = new_interpolation(volt[to_check])
    real_temp = temp[to_check]
    #Calculating absolute value of differences
    errors.append(np.abs(interpolated_temp - real_temp))

  #Processing statistics
  error=np.mean(errors)
  error_std=np.std(errors)

  print(f"The error is {error:.4f} +/- {error_std:.4f}")


lakeshore(V,dat)
