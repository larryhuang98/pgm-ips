Here, we use imin=5 to calculate the energy from IPS functional for each configurations from PME trajectory

The input is as follows:

```
  single point calc.
 &cntrl
   imin=5,maxcyc=1,
   ntb=1,
   ntp=0,
   ntc=2, ntf=2, tol=0.000001,
   cut=10.,
   ntpr=100, ntwr=100, ntwx=100,
   dt=0.001,
   ipgm=1,ips=1,
 /
 &ewald
  skinnb=0.,ew_coeff=0.4,nfft1=50,nfft2=50,nfft3=50,order=8,vdwmeth=0
 /
 &pol_gauss
   pol_gauss_verbose=0,ee_dsum_cut=10.0,pol_gauss_ips=1,
   dipole_scf_tol=0.0001,dipole_scf_init=1,dipole_scf_init_order=3,dipole_scf_init_step=2,
   scf_solv_opt=1,scf_sor_niter=100,scf_sor_coefficient=0.65,
   scf_cg_niter=50,scf_local_niter=3,scf_local_cut=4.0
 /
```
