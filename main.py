from extract.extract_csv import extract_sales_data
from transform.transform_sales import transform_sales
from load.load_postgress import load_to_db
from config import RAW_DATA_PATH

def main():
    #Extract
    df = extract_sales_data(RAW_DATA_PATH)

    if df is not None:
        print("Extraction Successfull")
        print(df.head())
        print(df.info())
    
        #Transform
        df_transformed = transform_sales(df)
        print("Transformation successul")
        print(df_transformed.head())
        print(df_transformed.info())

        #Filter orders above $50 revenue
        df_filtered = df_transformed[df_transformed["revenue"] > 50]
        print("orders with revenue > $50")
        print(df_filtered)

        #Group by product for analytics
        df_summary = df_transformed.groupby("product")["revenue"].sum().reset_index()
        print("Revenue by product")
        print(df_summary)

        #load
        load_to_db(df_transformed)

if __name__ == "__main__":
    main()