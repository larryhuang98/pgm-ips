#!/usr/bin/env python3
import os
import numpy as np
import matplotlib.pyplot as plt
import glob

cutoff_folders = ['cut6', 'cut7', 'cut8', 'cut9', 'cut10']
output_dir = 'comparison_plots'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for folder in cutoff_folders:
    cutoff_value = folder.replace('cut', '')
    
    pme_file = os.path.join(folder, 'g_OO_pme.dat')
    ips_file = os.path.join(folder, 'g_OO_ips.dat')
    
    if not (os.path.exists(pme_file) and os.path.exists(ips_file)):
        print(f"Warning: Missing data files in {folder}, skipping...")
        continue
    try:
        pme_data = np.loadtxt(pme_file)
        ips_data = np.loadtxt(ips_file)
    except Exception as e:
        print(f"Error loading data from {folder}: {e}")
        continue
    plt.figure(figsize=(10, 6))
    plt.plot(pme_data[:, 0], pme_data[:, 1], label='PME', linewidth=2, color='blue')
    plt.plot(ips_data[:, 0], ips_data[:, 1], label='IPS', linewidth=2, color='red', linestyle='--')
    plt.xlabel('r (Å)', fontsize=14)
    plt.ylabel('g(r)', fontsize=14)
    plt.title(f'O-O Radial Distribution Function with cut-off distance: {cutoff_value} Å', fontsize=16)
    plt.legend(fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    output_file = os.path.join(output_dir, f'g_OO_comparison_{folder}.png')
    plt.savefig(output_file, dpi=300)
    plt.close()
