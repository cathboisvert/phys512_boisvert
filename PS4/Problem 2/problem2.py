## Problem 2

## Use Newton's method or LM to find best fit parameters using numerical derivatives. 
## Report the best-fit parameters and their errors 

import numpy as np
import camb
from matplotlib import pyplot as plt
import time

open("/Users/catherineboisvert/COM_PowerSpect_CMB-TT-full_R3.01.txt")

# How to implement:
#  1. Start with a guess for the parameters: m0
#  2. Calculate model A(m0) and local gradient Am
#  3. Solve linear system: Am.trans()*N.inv()*Am*delm = Am.trans()*N.inv()*r
#.     ---> I'm assuming this means solve for delm so that we can update the parameters. 
#  4. Set m0 -> m0+delm
#  5. Repeat until delm is "small". For chisq, change should always be <<1

#The starting guess, m0, could be the parameters from Jon's script. 
m0=np.asarray([69,0.022,0.12,0.06,2.1e-9,0.95])

#This will probably be the same as in previous code.  
def get_spectrum(pars,lmax=3000):
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

#Getting our numerical derivatives
def get_derivs(pars, lmax=3000):
    #This is the delta between steps
    delta=pars/100
    #This allows us to get the original y-values
    cmb=get_spectrum(pars,lmax)
    
    #Adding delta to the double sided derivative
    cmb_p=np.zeros([len(cmb), len(pars)])
    cmb_p_neg=np.zeros([len(cmb),len(pars)])
    
    for i in range(len(pars)):
        pars_curr=pars
        #adding deltas and getting spectrum
        pars_curr[i]=pars[i]+delta[i]
        cmb_p[:,i]=get_spectrum(pars_curr,lmax)
        #subtracting deltas and getting spectrum
        pars_curr[i]=pars[i]-delta[i]
        cmb_p_neg[:,i]=get_spectrum(pars_curr,lmax)
    
    derivs=(cmb_p-cmb_p_neg)/(2*delta)
    return cmb, derivs #returns the y values and the derivatives
    
#updating lamda
def update_lamda(lamda,success):
    if success:
        lamda==0
    else:
        if lamda==0:
            lamda=1
        else:
            lamda=lamda*1.5**2
    return lamda
    
def get_matrices(m,fun,x,y,Ninv=None):
    model,derivs=get_derivs(m)
    model=model[:len(y)]
    derivs=derivs[:len(y),:]
    resid=y-model
    
    if Ninv is None:
        lhs=derivs.T@derivs
        rhs=derivs.T@resid
        chisq=np.sum(resid**2)
    else:
        lhs=derivs.T@Ninv@derivs
        rhs=derivs.T@(Ninv@resid)
        chisq=resid.T@Ninv@resid
    return chisq,lhs,rhs    


def fit_lm_clean(m,fun,x,y,Ninv=None,niter=10,chitol=0.01):
    lamda=0
    chisq,lhs,rhs=get_matrices(m,fun,x,y,Ninv)
    for i in range(niter):
        lhs_inv=linv(lhs,lamda)
        dm=lhs_inv@rhs
        chisq_new,lhs_new,rhs_new=get_matrices(m+dm,fun,x,y,Ninv)
        errs=np.sqrt(np.diag(lhs_inv))
        if chisq_new<chisq:  
            #accept the step
            #check if we think we are converged - for this, check if 
            #lamda is zero (i.e. the steps are sensible), and the change in 
            #chi^2 is very small - that means we must be very close to the
            #current minimum
            if lamda==0 and m[3]>0.01:
                if (np.abs(chisq-chisq_new)<chitol):
                    print(np.abs(chisq-chisq_new))
                    print('Converged after ',i,' iterations of LM')
                    return m+dm
            chisq=chisq_new
            lhs=lhs_new
            rhs=rhs_new
            m=m+dm
            lamda=update_lamda(lamda,True)
        else:
            lamda=update_lamda(lamda,False)
            print('on iteration ',i,' chisq is ',chisq,' with step ',dm,' and lamda ',lamda)
    return m,errs,lhs

def linv(mat,lamda):
    mat=mat+lamda*np.diag(np.diag(mat)) #finds inverse
    return np.linalg.inv(mat)

lamda=0 #initialize lambda

data=np.loadtxt('COM_PowerSpect_CMB-TT-full_R3.01.txt',skiprows=1)
ell=data[:,0]
spec = data[:,1]
err = 0.5*(data[:,2]+data[:,3])

#inverse noise matrix
Ninv = np.linalg.inv(np.diag(err))

#Finding the initial chisq
model,derivs=get_derivs(m0)
model=model[:len(spec)]
resid=spec-model
chisq=np.sum((resid/err)**2)
print('initial chi^2:', chisq)

# Running the code
m_fit,error,lhs=fit_lm_clean(m0,get_spectrum,ell,spec,Ninv,niter=5)
print(m_fit)
print('dm error: ',error)
model_pred=get_spectrum(m_fit)
model_pred=model_pred[:len(spec)]
resid=spec-model_pred
chisq=np.sum((resid/errs)**2)
print(chisq)
print(lhs) #curvature matrix
#[69,0.022,0.12,0.06,2.1e-9,0.95]

