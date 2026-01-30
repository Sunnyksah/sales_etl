import pandas as pd

def extract_sales_data(file_path):

    try:
        df = pd.read_csv(file_path)
        print(f"Extracted {len(df)} rows from {file_path}")
        return df
    except FileNotFoundError:
        print(f"Error: File {file_path} not found")
        return None