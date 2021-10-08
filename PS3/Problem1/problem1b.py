"""
The next part requires that we take a step of length h, compare it to two steps
of length h/2, and use them to cancel out the leading-error order term from RK4.
Check the number of function evaluations needed for this method. 
"""
def rk4_stepd(fun,x,y,h):
  y1=rk4_step(fun,x,y,h)
  y2_first=rk4_step(fun,x,y,h/2)
  y2_second=rk4_step(fun,x+(h/2),y2_first,h/2)

  delt=y2_second-y1

  return y2_second + delt/15

y_init=1
x_stepperd=np.linspace(-20,20,66)
h=np.median(np.diff(x_stepperd))
y_stepperd=np.zeros(len(x_stepperd))
y_stepperd[0]=y_init
truth2=4.57605801504*np.exp(np.arctan(x_stepperd))

for i in range(len(x_stepperd)-1):
  y_stepperd[i+1]=rk4_stepd(func,x_stepperd[i],y_stepperd[i],h)

plt.plot(x_stepperd,y_stepperd,'*')
plt.plot(x_stepperd,truth2)

print(np.std(truth2-y_stepperd))


# calculating residuals
res_stepperd=abs(truth2-y_stepperd)
res_stepper=abs(truth-y)

plt.plot(x,res_stepper)
plt.plot(x_stepperd,res_stepperd)
