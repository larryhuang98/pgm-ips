import pandas as pd
import numpy as np

def calculate_rmsd(ref_data, target_data):
    if len(ref_data) != len(target_data):
        raise ValueError("Reference and target data must have the same length.")
    diff = ref_data - target_data
    return np.sqrt(np.mean(diff**2))

ref_file = 'cut10/g_OO_pme.dat'

try:
    ref_data = pd.read_csv(ref_file, sep='\s+', header=None, comment='#')
    ref_values = ref_data.iloc[:, 1]  # Adjust to select the second column (values of interest)
except FileNotFoundError:
    raise FileNotFoundError(f"Reference file not found: {ref_file}")
except pd.errors.ParserError:
    print(f"Error parsing {ref_file}. Check the file format and data consistency.")

rmsd_results = []

for job in range(6, 11):
    target_file = f'cut{job}/g_OO_pme.dat'
    
    try:
        target_data = pd.read_csv(target_file, sep='\s+', header=None, comment='#')
        target_values = target_data.iloc[:, 1]  # Adjust to select the second column (values of interest)
        
        rmsd_value = calculate_rmsd(ref_values, target_values)
        rmsd_results.append((f'cut{job}', rmsd_value))
        
    except FileNotFoundError:
        print(f"File not found: {target_file}. Skipping.")
    except ValueError as e:
        print(f"Error calculating RMSD for {target_file}: {e}")
    except pd.errors.ParserError:
        print(f"Error parsing {target_file}. Check the file format and data consistency.")

rmsd_df = pd.DataFrame(rmsd_results, columns=['Job', 'RMSD'])

rmsd_df.to_csv('rmsd_results.csv', index=False)

print("\nRMSD Results:")
print(rmsd_df)

