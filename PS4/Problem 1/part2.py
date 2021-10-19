## Problem 1 -- Jon's script
## Parameter change to [69, 0.022, 0.12, 0.06, 2.1e− 9, 0.95]

import numpy as np
import camb
from matplotlib import pyplot as plt
import time


def get_spectrum(pars,lmax=3000): #model
    #print('pars are ',pars)
    H0=pars[0]
    ombh2=pars[1]
    omch2=pars[2]
    tau=pars[3]
    As=pars[4]
    ns=pars[5]
    #Set up a new set of parameters for CAMB
    pars=camb.CAMBparams()
    #This function sets up CosmoMC-like settings, with one massive neutrino and helium set using BBN consistency
    pars.set_cosmology(H0=H0,ombh2=ombh2,omch2=omch2,mnu=0.06,omk=0,tau=tau)
    pars.InitPower.set_params(As=As,ns=ns,r=0)
    pars.set_for_lmax(lmax,lens_potential_accuracy=0)
    #calculate results for these parameters
    results=camb.get_results(pars)
    #get dictionary of CAMB power spectra
    powers=results.get_cmb_power_spectra(pars,CMB_unit='muK')
    cmb=powers['total']
    tt=cmb[:,0]    #you could return the full power spectrum here if you wanted to do say EE
    return tt[2:]




plt.ion()

pars=np.asarray([69,0.022,0.12,0.06,2.1e-9,0.95]) #setting ordering parameters

#have to add these lines in order to have access to the data
open("/Users/catherineboisvert/COM_PowerSpect_CMB-TT-full_R3.01.txt")
open("/Users/catherineboisvert/COM_PowerSpect_CMB-TT-binned_R3.01.txt")

planck=np.loadtxt('COM_PowerSpect_CMB-TT-full_R3.01.txt',skiprows=1)
ell=planck[:,0] #multipole
spec=planck[:,1] #variance of sky at this multipole
errs=0.5*(planck[:,2]+planck[:,3]); #average of lower uncertainty and upper uncertainty
model=get_spectrum(pars) #putting the parameters into the model. 
model=model[:len(spec)] #setting it the length of spec?
resid=spec-model #calculating residual between variance and model
chisq=np.sum( (resid/errs)**2) #calculating chisq
print("chisq is ",chisq," for ",len(resid)-len(pars)," degrees of freedom.")
#read in a binned version of the Planck PS for plotting purposes
planck_binned=np.loadtxt('COM_PowerSpect_CMB-TT-binned_R3.01.txt',skiprows=1)
errs_binned=0.5*(planck_binned[:,2]+planck_binned[:,3]);
plt.clf()
plt.plot(ell,model)
plt.errorbar(planck_binned[:,0],planck_binned[:,1],errs_binned,fmt='.')
plt.show()
