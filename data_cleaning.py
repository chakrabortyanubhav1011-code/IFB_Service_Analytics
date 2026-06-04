import pandas as pd

# LOAD EXCEL FILES

pending_df = pd.read_excel(
    "data/raw/fake_pending_calls_dataset.xlsx"
)

closure_df = pd.read_excel(
    "data/raw/fake_call_closure_dataset.xlsx"
)

css_df = pd.read_excel(
    "data/raw/fake_customer_satisfaction_dataset.xlsx"
)

# SHOW BASIC INFO

print("===== PENDING CALLS =====")
print(pending_df.info())

print("\n===== CLOSURE DATA =====")
print(closure_df.info())

print("\n===== CUSTOMER SATISFACTION =====")
print(css_df.info())

# REMOVE DUPLICATES

pending_df = pending_df.drop_duplicates()

closure_df = closure_df.drop_duplicates()

css_df = css_df.drop_duplicates()

# HANDLE MISSING VALUES

pending_df = pending_df.fillna("Unknown")

closure_df = closure_df.fillna("Unknown")

css_df = css_df.fillna("Unknown")

# STANDARDIZE COLUMN NAMES

pending_df.columns = (
    pending_df.columns
    .str.lower()
    .str.replace(" ", "_")
)

closure_df.columns = (
    closure_df.columns
    .str.lower()
    .str.replace(" ", "_")
)

css_df.columns = (
    css_df.columns
    .str.lower()
    .str.replace(" ", "_")
)

# CONVERT DATE COLUMNS

pending_df["call_book_date"] = pd.to_datetime(
    pending_df["call_book_date"],
    dayfirst=True,
    errors="coerce"
)

closure_df["call_book_date"] = pd.to_datetime(
    closure_df["call_book_date"],
    dayfirst=True,
    errors="coerce"
)

closure_df["closure_date"] = pd.to_datetime(
    closure_df["closure_date"],
    dayfirst=True,
    errors="coerce"
)

css_df["feedback_date"] = pd.to_datetime(
    css_df["feedback_date"],
    dayfirst=True,
    errors="coerce"
)

# SAVE CLEANED FILES

pending_df.to_csv(
    "data/cleaned/pending_calls_cleaned.csv",
    index=False
)

closure_df.to_csv(
    "data/cleaned/call_closure_cleaned.csv",
    index=False
)

css_df.to_csv(
    "data/cleaned/customer_satisfaction_cleaned.csv",
    index=False
)

print("\nDATA CLEANING COMPLETED SUCCESSFULLY")