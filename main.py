from extract.extract_csv import extract_sales_data
from transform.transform_sales import transform_sales
from load.load_postgress import load_sales_data
from load.db import get_db_engine
from config import RAW_DATA_PATH
from logger import logger

def main():
    logger.info("ETL Pipeline started")

    # EXTRACT
    df = extract_sales_data(RAW_DATA_PATH)

    if df is None:
        logger.error("Extraction failed. Pipeline stopped.")
        return
    else:
        logger.info(f"Extraction successful. Rows extracted: {len(df)}")

    #  TRANSFORM 
    df_transformed = transform_sales(df)
    logger.info(f"Transformation successful. Rows after transform: {len(df_transformed)}")

    #  FILTER & ANALYTICS 
    df_filtered = df_transformed[df_transformed["revenue"] > 50]
    logger.info(f"Filtered orders with revenue > $50: {len(df_filtered)} rows")

    df_summary = df_transformed.groupby("product")["revenue"].sum().reset_index()
    logger.info("Revenue by product:")
    logger.info(f"\n{df_summary}")

    # LOAD
    load_sales_data(df_transformed)
    logger.info("Data loaded into PostgreSQL successfully")

    engine = get_db_engine()
    load_sales_data(df, engine)

    logger.info("ETL Pipeline completed successfully")


if __name__ == "__main__":
    main()
