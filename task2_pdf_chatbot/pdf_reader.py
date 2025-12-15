import pdfplumber

def extract_pdf(path: str):
    full_text = ""
    tables = []

    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                full_text += page_text + "\n"

            table = page.extract_table()
            if table:
                tables.append(table)

    return full_text, tables
