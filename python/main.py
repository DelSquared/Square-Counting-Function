import numpy as np 
import matplotlib.pyplot as plt 

sigma = np.array([])
sgm=0
n=0
n2=n*n

N=1000

Z=range(N)

for _ in Z:
  if _==n2:
    sgm+=1
    n+=1
    n2=n*n
  sigma=np.append(sigma,[sgm])

fig=plt.figure()
plt.plot(Z,sigma,label=r'$\sigma(n)$')
plt.plot(Z,np.sqrt(Z)+np.ones_like(Z),label=r'$\sqrt{x}+1$')
plt.plot(Z,(np.sqrt(Z)+np.sqrt(Z+np.ones_like(Z))+np.ones_like(Z))/2,label=r'$\frac{\sqrt{x}+1+\sqrt{x+1}}{2}$')
plt.plot(Z,np.sqrt(Z+np.ones_like(Z)),label=r'$\sqrt{x+1}$')
plt.plot(Z,np.append([1],1/((np.sqrt(Z[1:])+np.sqrt(Z[1:]+np.ones_like(Z[1:]))+np.ones_like(Z[1:]))/2)),label=r'$\rho_\sigma (x)$')
plt.grid()
plt.legend()
plt.savefig("plot.png")
plt.close(fig)
