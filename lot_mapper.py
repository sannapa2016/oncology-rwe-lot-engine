import pandas as pd

def map_lines_of_therapy(input_file='oncology_claims_raw.csv'):
    df = pd.read_csv(input_file)
    df['claim_date'] = pd.to_datetime(df['claim_date'])
    
    # Sort by patient and date
    df = df.sort_values(['patient_id', 'claim_date'])
    
    # Identify drug switches
    df['prev_drug'] = df.groupby('patient_id')['drug_name'].shift(1)
    df['is_new_line'] = (df['drug_name'] != df['prev_drug']) & (df['prev_drug'].notnull())
    
    # Cumulative sum to create Line Number
    df['lot_number'] = df.groupby('patient_id')['is_new_line'].cumsum() + 1
    
    return df

if __name__ == "__main__":
    lot_df = map_lines_of_therapy()
    lot_df.to_csv('mapped_lot_data.csv', index=False)
    print("LOT Mapping Complete. Samples saved to mapped_lot_data.csv")
