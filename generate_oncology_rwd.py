import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_data(n_patients=500):
    np.random.seed(42)
    data = []
    
    drugs = {
        'L1_Standard': ['Pembrolizumab', 'Nivolumab'],
        'L2_Standard': ['Docetaxel', 'Cabazitaxel']
    }

    for p_id in range(1000, 1000 + n_patients):
        # Random start date in 2024
        start_date = datetime(2024, 1, 1) + timedelta(days=np.random.randint(0, 180))
        
        # Line 1: 4 to 8 months of treatment
        l1_drug = np.random.choice(drugs['L1_Standard'])
        l1_duration = np.random.randint(4, 9)
        for i in range(l1_duration):
            data.append([p_id, start_date + timedelta(days=i*30), l1_drug])
        
        # Line 2: 60% of patients progress to L2 after a 30-day gap
        if np.random.rand() < 0.6:
            l2_start = start_date + timedelta(days=(l1_duration * 30) + 30)
            l2_drug = np.random.choice(drugs['L2_Standard'])
            l2_duration = np.random.randint(3, 6)
            for j in range(l2_duration):
                data.append([p_id, l2_start + timedelta(days=j*30), l2_drug])

    df = pd.DataFrame(data, columns=['patient_id', 'claim_date', 'drug_name'])
    df.to_csv('oncology_claims_raw.csv', index=False)
    print("Successfully generated oncology_claims_raw.csv")

if __name__ == "__main__":
    generate_data()
