from sqlalchemy import create_engine

def load_to_db(df):

    if df is None or df.empty:
        print("No data to load")
        return
    
    #Database connection

    db_url = "postgresql://postgres:password@localhost:5432/salesdb"

    #create SQLALchemy engine
    engine = create_engine(db_url)

    try:
        df.to_sql("sales", engine, if_exists = "replace", index = False)
        print(f"Loaded {len(df)} rows into postgreSQL table 'sales'")
    except Exception as e:
        print("Error loading to DB: ", e)