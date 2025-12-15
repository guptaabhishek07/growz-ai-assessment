import pandas as pd

def normalize(df):
    df.columns = (
        df.columns.str.lower()
        .str.replace(" ", "_")
        .str.replace("(pi)", "")
    )

    numeric_cols = [
        "qty", "unit_price", "discount_%",
        "tax_%", "line_subtotal", "line_total"
    ]

    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    return df
