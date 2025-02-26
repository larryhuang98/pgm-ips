This repository provides input files, analysis scripts and some output files for reproducing the results from our paper "Isotropic periodic sum for polarizable Gaussian Multipole model"


AMBERTOOLS 2025 is required to do all the simulations.

To use the pGM model, one need to set `ipgm=1` under cntrl section. To use the IPS to replace PME in pGM model, one need to specify `ips=1` under cntrl section and add `pol_gauss_ips=1` under pol_gauss section. To enable dipole printing, one need to set `dipole_print=n`, where the dipole moment will be printed every n frames. As the pGM model is still under extensive development, we will update the AMBER manual once we finalize the model.
