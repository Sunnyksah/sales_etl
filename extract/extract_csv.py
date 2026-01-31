
import pandas as pd
from logger import logger

def extract_sales_data(file_path):
    try:
        logger.info(f"Starting extraction from {file_path}")

        df = pd.read_csv(file_path)

        logger.info(f"Extraction Successful. Rows extracted: {len(df)}")

        return df
    
    except FileNotFoundError:
        logger.error(f"File not found:{file_path}")
        return None
    
    except Exception as e:

        logger.error(f"Unexcepted error during extraction:{e}")

        return None


