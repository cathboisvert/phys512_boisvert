# Problem 4 - redoing q3 with new constraints

import numpy as np
import camb
from matplotlib import pyplot as plt

def get_chisq(data,model,sigma):
    chisq=np.sum(((data-model)/sigma)**2)
    return chisq

def get_step(step_size):
    step=np.random.randn(len(step_size))*step_size
    return step

def get_spectrum(pars,lmax=2507):
    H0=pars[0]
    ombh2=pars[1]
    omch2=pars[2]
    tau=pars[3]
    As=pars[4]
    ns=pars[5]
    pars=camb.CAMBparams()
    pars.set_cosmology(H0=H0,ombh2=ombh2,omch2=omch2,mnu=0.06,omk=0,tau=tau)
    pars.InitPower.set_params(As=As,ns=ns,r=0)
    pars.set_for_lmax(lmax,lens_potential_accuracy=0)
    results=camb.get_results(pars)
    powers=results.get_cmb_power_spectra(pars,CMB_unit='muK')
    cmb=powers['total']
    tt=cmb[:,0]    #you could return the full power spectrum here if you wanted to do say EE
    return tt[2:]

#initial parameters, where we'll start our MCMC chain
pars=np.asarray([69,0.022,0.12,0.0540,2.1e-9,0.95])
npars=len(pars)

#getting data, model, and initial chisq
data = np.loadtxt('COM_PowerSpect_CMB-TT-full_R3.01.txt',skiprows=1)
ell=data[:,0]
spec=data[:,1]
errs=0.5*(data[:,2]+data[:,3]);
model=get_spectrum(pars)
model=model[:len(spec)]
chisq=get_chisq(spec,model,errs)
print('initial chi^2:', chisq)

#Setup an array for chisq so that we keep track of its history while walking around in parameter space. 
nstep=5000
chain=np.zeros([nstep,npars])
chisq_vec=np.zeros(nstep)

T=1.0
# step a large amount of times
# rejecting or accepting based on some probability, e^(-0.5*delt_chisq)
# improving chisq = improving our fit
j=0
for i in range(nstep):
    new_pars=pars+cov_tau@np.random.randn(npars)
    model=get_spectrum(new_pars)
    model=model[:len(spec)]
    chisq_new=get_chisq(spec,model,errs)
    delta_chisq=chisq_new-chisq
    if (np.exp(-0.5*(delta_chisq)/T)>np.random.rand(1)): #accept the step
        if new_pars[3]>0.0466 and new_pars[3]<0.0614:
            pars=new_pars
            chisq=chisq_new
            j+=1
    chisq_vec[i]=chisq
    chain[i,:]=pars
    
    print('On iteration ',i,' chisq is ',chisq_new,' with step ',cov_tau@np.random.randn(npars),'and parameters',new_pars)
    if i!=0:
        print('% of acccepted steps is',100*j/i,'%')


