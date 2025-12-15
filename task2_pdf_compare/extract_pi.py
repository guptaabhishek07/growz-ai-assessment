import pdfplumber
import pandas as pd

def extract_pi(path="Proforma_Invoice_2025-12-12.pdf"):
    rows = []
    with pdfplumber.open(path) as pdf:
        first = pdf.pages[0]
        table = first.extract_table()

        for row in table[1:]:
            rows.append(row)

    df = pd.DataFrame(rows, columns=table[0])
    return df
