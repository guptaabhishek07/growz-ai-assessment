import pandas as pd
from pyxlsb import open_workbook

def load_sales_data(path="Sales & Active Stores Data.xlsb"):
    # Load XLSB file
    df = pd.read_excel(path, engine="pyxlsb")

    # --- FIX COLUMN NAME NORMALIZATION ---
    df.columns = (
        df.columns
        .astype(str)
        .str.strip()                          # remove leading/trailing spaces
        .str.replace("\u00A0", " ", regex=False)  # replace non-breaking spaces
        .str.replace(r"\s+", " ", regex=True) # collapse multiple spaces
        .str.title()                          # convert to Title Case
    )

    # Optional: convert "Month" column if exists
    if "Month" in df.columns:
        df["Month"] = pd.to_datetime(df["Month"], errors="ignore")

    return df
