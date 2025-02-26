import os
os.environ['OPENBLAS_NUM_THREADS'] = '1'
import numpy as np
import matplotlib.pyplot as plt

try:
    # Load the data
    ips = np.loadtxt("etot-ips-high")
    pme = np.loadtxt("etot-pme-high")

    # Create the plot
    plt.plot(ips[0:,0], ips[:,1]-ips[20,1], label='IPS')
    plt.plot(pme[0:,0], pme[:,1]-pme[20,1], label='PME')
    # Add labels and title
    plt.xlabel('Time (ps)')
    plt.ylabel('Relative Total Energy (kcal/mol)')
    plt.xlim([0,1000])
    # Add grid and legend
    plt.ylim([-2,2])
    plt.grid(True)
    plt.legend()

    # Save the plot with higher DPI for better quality
    plt.savefig("compare.png", dpi=600, bbox_inches='tight')
    plt.show()

except Exception as e:
    print(f"An error occurred: {e}")
