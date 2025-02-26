#!/bin/bash

# Iterate over different values of ee_dsum_cut
for ee_dsum_cut in 6 7 8 9 10
do
  # Loop over 10 runs for each ee_dsum_cut
  for i in {1..10}
  do
    # For IPS
    cat > cpptraj_input_ips_${ee_dsum_cut}_run$i.in <<EOF
# Load the topology file and trajectory for the current IPS run
parm pGM.prmtop
trajin job_${ee_dsum_cut}/run${i}/rcut${ee_dsum_cut}_run${i}.nc mdvel job_${ee_dsum_cut}/run${i}/rcutv${ee_dsum_cut}_run${i}.nc

# Calculate velocity autocorrelation for water oxygen atoms (IPS)
velocityautocorr vel-corr :WAT@O out vel-ips${ee_dsum_cut}_run${i}.txt diffout diff-ips${ee_dsum_cut}_run${i}.txt maxlag 5000 tstep 0.001 norm

# Run the analysis for IPS
go
EOF

    # Run cpptraj for the IPS results
    cpptraj -i cpptraj_input_ips_${ee_dsum_cut}_run$i.in

    # For PME
    cat > cpptraj_input_pme_${ee_dsum_cut}_run$i.in <<EOF
# Load the topology file and trajectory for the current PME run
parm pGM.prmtop
trajin job_${ee_dsum_cut}/run${i}/pme_run${i}.nc mdvel job_${ee_dsum_cut}/run${i}/pmev_run${i}.nc

# Calculate velocity autocorrelation for water oxygen atoms (PME)
velocityautocorr vel-corr :WAT@O out vel-pme${ee_dsum_cut}_run${i}.txt diffout diff-pme${ee_dsum_cut}_run${i}.txt maxlag 5000 tstep 0.001 norm

# Run the analysis for PME
go
EOF

    # Run cpptraj for the PME results
    cpptraj -i cpptraj_input_pme_${ee_dsum_cut}_run$i.in
  done
done
