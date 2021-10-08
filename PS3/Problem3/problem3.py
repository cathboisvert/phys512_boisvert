###Problem 3, least squares fit, part b) -- objective to carry out the fit and find parameters

import numpy as np
from matplotlib import pyplot as plt

open("/Users/catherineboisvert/dish_zenith.txt")
dat=np.loadtxt("dish_zenith.txt") #this puts the entire data into an array
#print(dat)

# first row = x, second row = y, third row = z

dat_points=len(dat) # counts how many rows in the dataset, i.e. how many data points

# putting data in arrays
x_data=np.array(dat[:,0])
y_data=np.array(dat[:,1])
z_data=np.array(dat[:,2])


ndata=dat_points # number of data points in the file
npoly=4 # number of columns
A=np.zeros([ndata,npoly])

#setting up matrix A
A[:,0]=1.0 # first column of A, all 1
A[:,1]=A[:,0]*x_data # second column of A, all the x values of data
#print(A[:,1])
A[:,2]=A[:,0]*y_data # third column of A, all the y values of data
A[:,3]=A[:,1]*x_data + A[:,2]*y_data # fourth column of A, all the z values of data

#carrying out the fit
A=np.matrix(A)
d=np.matrix(z_data).transpose()
lhs=A.transpose()*A
rhs=A.transpose()*d
pars=np.linalg.inv(lhs)*rhs

#parameters
p0=pars[0,0]
p1=pars[1,0]
p2=pars[2,0]
p3=pars[3,0]

p = [p0,p1,p2,p3]


a=p[3]
x0=-p[1]/(2*a)
y0=-p[2]/(2*a)
z0=p[0]-(a*x0**2)-(a*y0**2)

print('a=',a,', x0=',x0,', y0=',y0,', z0=',z0)

#using noise to get uncertainty on a
z_pred=a*((x_data-x0)**2+(y_data-y0)**2)-z0
noise=np.std(z_data-z_pred)
print('noise is',noise)
N=np.eye(len(z_data))*noise**2
Ninv=np.eye(len(x_data))*noise**-2

err=np.linalg.inv(A.transpose()@N@A)
pars_errs=np.sqrt(np.diag(err))


print('parameter errors are',pars_errs)

print('focal length = ', 1/(4*a), '+/-', (pars_errs[3]/a)*(1/(4*a)))

#part c of q3

#di = np.sqrt(np.diag(np.linalg.inv(lhs)))
#print(di)

#print('focal length = ', 1/(4*a), '+/-', (di[3]/a)*(1/(4*a)))
