x=np.linspace(0,4999,5000)
#print(x)
finding_pars= np.loadtxt('planck_chain.txt')

print(finding_pars)

final_pars=np.zeros([6])

final_pars[0]=np.mean(finding_pars[:,1])
final_pars[1]=np.mean(finding_pars[:,2])
final_pars[2]=np.mean(finding_pars[:,3])
final_pars[3]=np.mean(finding_pars[:,4])
final_pars[4]=np.mean(finding_pars[:,5])
final_pars[5]=np.mean(finding_pars[:,6])

print(final_pars)

chisq_avg=np.mean(finding_pars[:,0])
print(chisq_avg)

plt.plot(x,chain[:,5])
#plt.plot(x,chisq_vec)

# saving chain to document
import numpy as np

file_mcmc_params=np.empty([nstep,7])
file_mcmc_params[:,0]=chisq_vec
file_mcmc_params[:,1]=chain[:,0]
file_mcmc_params[:,2]=chain[:,1]
file_mcmc_params[:,3]=chain[:,2]
file_mcmc_params[:,4]=chain[:,3]
file_mcmc_params[:,5]=chain[:,4]
file_mcmc_params[:,6]=chain[:,5]

np.savetxt('planck_chain.txt',file_mcmc_params)

#finding mean value of dark energy
mean_dm_a=np.mean(finding_pars[:,3])
mean_dm_b=np.mean(finding_pars[:,2])
print('Baryon density is ',mean_dm_b,' and Dark matter density is ',mean_dm_a)
err_dm_a=np.std(finding_pars[:,3])
err_dm_b=np.std(finding_pars[:,2])
print('Their respective uncertainties are ',err_dm_b,' and ',err_dm_a)
mean_h0=np.mean(finding_pars[:,1])
print(mean_h0)

h=mean_h0/100
print(h)
hsq=h**2
mean_dm_b=mean_dm_b/hsq
mean_dm_a=mean_dm_a/hsq
dark_energy=1-mean_dm_b-mean_dm_a
print(dark_energy)

err_dm_a=err_dm_a/hsq
err_dm_b=err_dm_b/hsq
err_dark=np.sqrt((err_dm_b)**2 + (err_dm_a)**2)
print(err_dark)
