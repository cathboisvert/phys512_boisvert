# Importance sampling for Problem 4

def prior_chisq(pars,par_priors,par_errs):
    if par_priors is None:
        return 0
    par_shifts=pars-par_errs
    return np.sum((par_shifts/par_errs)**2)

print(np.mean(chisq_vec))

#defining expected pars
expected_pars=np.zeros([6])
expected_pars[0]=np.mean(chain[:,0]) #chain is the newest chain, i.e. the one with constraints.
expected_pars[1]=np.mean(chain[:,1])
expected_pars[2]=np.mean(chain[:,2])
expected_pars[3]=np.mean(chain[:,3])
expected_pars[4]=np.mean(chain[:,4])
expected_pars[5]=np.mean(chain[:,5])
print(expected_pars)

#defining errors
par_errs=np.zeros([6])
par_errs[0]=np.std(chain[:,0])
par_errs[1]=np.std(chain[:,1])
par_errs[2]=np.std(chain[:,2])
par_errs[3]=np.std(chain[:,3])
par_errs[4]=np.std(chain[:,4])
par_errs[5]=np.std(chain[:,5])
print(par_errs)

weight=np.zeros(nstep)
chivec=np.zeros(nstep)
k=[]
for i in range(nstep):
    chisq=prior_chisq(finding_pars[i,1:],expected_pars,par_errs) #finding_pars is from first chain
    chivec[i]=chisq
    #weight[i]=np.exp(-0.5*chisq)
chivec=chivec-chivec.mean()
weight=np.exp(-0.5*(prior_chisq(finding_pars[:,4],expected_pars[3],par_errs[3])))
#weight=np.exp(-0.5*(prior_chisq(final_pars[3],expected_pars[3],par_errs[3])))

#print(finding_pars[:,1:])

print(chivec)
plt.plot(x,chivec)


for i in range(len(par_errs)):
    print('importance sampled parameter ',i,' has mean ',np.sum(weight*chain[:,i])/np.sum(weight))
