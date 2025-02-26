#!/bin/bash

# Loop through folders job_6 to job_10
for i in {6..10}
do
    # Create input file for rcut6.out
    cat << EOF > job_${i}/cpptraj_g_OO_rcut6.in
parm pGM.prmtop
trajin job_${i}/rcut${i}.nc mdvel job_${i}/rcutv${i}.nc
velocityautocorr vel-corr :WAT@O out pme${i}.txt diffout diff-pme${i}.txt maxlag 5000 tstep 0.001 norm
run
EOF

done

