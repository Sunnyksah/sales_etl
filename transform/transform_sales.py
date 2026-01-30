import pandas as pd

def transform_sales(df):

    if df is None:
        return None
    
    #Remove duplicate
    df = df.drop_duplicates()

    #Fix data types
    df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
    df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")
    df["price"] = pd.to_numeric(df["price"], errors="coerce")

    #Handle missing values
    df = df.dropna(subset=["order_id", "customer_id", "product"])
    df["quantity"] = df["quantity"].fillna(0)
    df["price"] = df["price"].fillna(0)

    #create new column
    df["revenue"] = df["quantity"] * df["price"]

    #Round revenue
    df["revenue"] = df["revenue"].round(2)

    #Rename columns for database
    df = df.rename(columns={
        "order_id":"id",
        "customer_id":"customer",
        "order_date":"date"
    })

    return df