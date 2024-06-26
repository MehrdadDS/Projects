import pandas as pd
from sqlalchemy import create_engine


# Example usage
db_url = 'mysql+pymysql://root:123456@localhost/stocks'


def append_to_sql(df, db_url, schema, table):
    """
    Appends a DataFrame to a SQL table.

    Parameters:
    df (pd.DataFrame): The DataFrame to append.
    db_url (str): The database URL.
    schema (str): The schema name.
    table (str): The table name.
    """
    # Create the SQLAlchemy engine
    engine = create_engine(db_url)

    # Append the DataFrame to the SQL table
    with engine.connect() as connection:
        df.to_sql(name=table, con=engine, if_exists='append', index=False)


#df = pd.read_excel('Book1.xlsx')
#append_to_sql(df, db_url, 'stock', 'historical_data')
