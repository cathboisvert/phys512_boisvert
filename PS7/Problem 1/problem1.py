import numpy as np
import random
a=random.randint(0,10**8) #same range as Jon's C RNG
n=30250 #nunber of RNs in Jon's script

random_py=np.empty([n,3])

#creating coordinates
for i in range(n):
    random_py[i,0]=random.randint(0,10**8)
    random_py[i,1]=random.randint(0,10**8)
    random_py[i,2]=random.randint(0,10**8)

np.savetxt('python_RNG.txt',random_py)

#x,y,z
xs=[]
ys=[]
zs=[]
for i in range(len(dat)):
    xs.append(random_py[i,0])
    ys.append(random_py[i,1])
    zs.append(random_py[i,2])

xs=np.asarray(xs)
ys=np.asarray(ys)
zs=np.asarray(zs)

print(len(random_py))

plt.plot(a*xs+b*ys,zs,'.')
