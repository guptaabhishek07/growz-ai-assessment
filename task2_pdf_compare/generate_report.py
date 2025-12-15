import pandas as pd

def generate_report(po_df, pi_df, output="discrepancy_report.csv"):
    merged = po_df.merge(pi_df, on="sku", suffixes=("_po", "_pi"))
    merged.to_csv(output, index=False)
    return output
