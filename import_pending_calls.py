import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus

# Read CSV
df = pd.read_csv(
    r"D:\IFB-Service-Analytics\Data\Cleaned\pending_calls_cleaned.csv"
)

# Convert datetime columns
df['call_book_date'] = pd.to_datetime(df['call_book_date'])

df['scheduled_date'] = pd.to_datetime(
    df['scheduled_date'],
    format='%d-%m-%Y %H:%M'
)

# Encode password
password = quote_plus("ZXasQW12#$")

# MySQL connection
engine = create_engine(
    f"mysql+pymysql://root:{password}@localhost/ifb_service_analytics"
)

# Import data
df.to_sql(
    name="pending_calls",
    con=engine,
    if_exists="append",
    index=False
)

print("Pending calls imported successfully!")