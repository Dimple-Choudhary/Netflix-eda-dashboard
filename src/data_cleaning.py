# src/data_cleaning.py
import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Perform data cleaning steps:
    - Handle nulls
    - Parse dates
    - Standardize text
    """
    
    df = df.copy()

    # Date parsing
    df["date_added"] = pd.to_datetime(df["date_added"], errors="coerce")

    # Text standardization
    df["type"] = df["type"].str.lower().str.strip()
    df["rating"] = df["rating"].str.strip()

    # Fill missing values
    df["country"] = df["country"].fillna("Unknown")


    return df
