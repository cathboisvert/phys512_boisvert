import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

open("/Users/catherineboisvert/rand_points.txt")
dat=np.loadtxt("rand_points.txt") #this puts the entire data into an array

print(dat)
print(len(dat))

print(dat[0])
print(dat[0])

#x,y,z
x=[]
y=[]
z=[]
for i in range(len(dat)):
    x.append(dat[i,0])
    y.append(dat[i,1])
    z.append(dat[i,2])

x=np.asarray(x)
y=np.asarray(y)
z=np.asarray(z)

#print(x)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(xs=x,ys=y,zs=z)
#ax.can_zoom()
#for ii in range(0,360,1):
        #ax.view_init(elev=10., azim=ii)
        #savefig("movie%d.png" % ii)

#3D not working? doing it in 2D
plt.figure()        
a=0.2
b=0.1
plt.plot(a*x+b*y,z,'.')
