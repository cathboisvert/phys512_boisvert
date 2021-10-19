s=np.random.randn(6)
curv=lhs
#print(curv)
#print('....')
cov=np.linalg.inv(curv)
#cov=linv(curv,lamda)
#print(cov)
#curv is now a 6x6 matrix
cov=np.linalg.cholesky(cov)
print('...')
print(cov)
print('...')
print(np.random.randn(6))
print('...')
print(cov@np.random.randn(6))



#Now I will need to print these best-fit parameters and their errors in planck_fit_params.txt

file_bf_params=np.empty([len(m_fit),2])
file_bf_params[:,0]=m_fit
file_bf_params[:,1]=error

np.savetxt('planck_fit_params.txt',file_bf_params)
