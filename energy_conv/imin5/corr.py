import numpy as np
import matplotlib.pyplot as plt

ips_data = np.loadtxt('ips-ene')
pme_data = np.loadtxt('pme-ene')

if len(ips_data) != len(pme_data):
    raise ValueError("The files do not have the same number of data points.")

correlation = np.corrcoef(ips_data, pme_data)[0, 1]

plt.figure(figsize=(8, 6), dpi=300)
plt.scatter(ips_data, pme_data, alpha=0.6, s=10, c='dodgerblue', edgecolors='k', linewidth=0.3)
plt.xlabel('IPS Energy', fontsize=14)
plt.ylabel('PME Energy', fontsize=14)
plt.title(f'Correlation between IPS and PME Energy: {correlation:.4f}', fontsize=16)
plt.grid(True, linestyle='--', alpha=0.5)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.savefig("crl.png", bbox_inches='tight', dpi=500)

print(f"Correlation coefficient: {correlation:.6f}")


