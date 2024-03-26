import pandas as pd
import glob
from pathlib import Path
from fpdf import FPDF

filepaths = glob.glob("Invoices/*.xlsx")

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    pdf.set_font(family="times", style="B",size=16)
    filename = Path(filepath).stem
    invoice_nr = filename.split("-")[0]
    pdf.cell(w=50,h=8, txt=f"Invoice nr.{invoice_nr}")
    pdf.output(f"PDFS/{filename}.pdf")