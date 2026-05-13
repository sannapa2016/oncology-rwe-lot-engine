import pandas as pd

def calculate_ttnt(input_file='mapped_lot_data.csv'):
    df = pd.read_csv(input_file)
    df['claim_date'] = pd.to_datetime(df['claim_date'])
    
    # Get the start date of each LOT
    lot_starts = df.groupby(['patient_id', 'lot_number'])['claim_date'].min().unstack()
    
    # TTNT is start of L2 minus start of L1
    if 1 in lot_starts.columns and 2 in lot_starts.columns:
        lot_starts['TTNT_L1_to_L2'] = (lot_starts[2] - lot_starts[1]).dt.days
        
        # Filter out patients who haven't progressed to L2
        progression_data = lot_starts.dropna(subset=['TTNT_L1_to_L2'])
        
        median_ttnt = progression_data['TTNT_L1_to_L2'].median()
        print(f"--- Real-World Evidence Summary ---")
        print(f"Total Patients Analyzed: {len(lot_starts)}")
        print(f"Patients Progressed to L2: {len(progression_data)}")
        print(f"Median Time to Next Treatment (TTNT): {median_ttnt} days")
    else:
        print("Insufficient data to calculate TTNT.")

if __name__ == "__main__":
    calculate_ttnt()
