import pandas as pd

def compare(po_df, pi_df):
    merged = po_df.merge(pi_df, on="sku", suffixes=("_po", "_pi"))

    fields = ["qty", "unit_price", "discount_%", "tax_%", "line_total"]

    reports = []

    for _, row in merged.iterrows():
        sku = row["sku"]
        issues = []

        for field in fields:
            po_val = row[f"{field}_po"]
            pi_val = row[f"{field}_pi"]

            if abs((pi_val or 0) - (po_val or 0)) > 0.01:
                issues.append(f"{field} mismatch: PO={po_val} PI={pi_val}")

        reports.append({
            "sku": sku,
            "issues": issues
        })

    return reports
