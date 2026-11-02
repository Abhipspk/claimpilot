import sys
from datetime import date

def build_invoice_line(invoice_id,customer,amount):
    today=date.today()
    return f"{today} | {invoice_id} | {customer} | Rs {amount:,.2f}"

if __name__ == "__main__":
    print("Python running from:", sys.executable)
    print(build_invoice_line("INV-1001", "Acme Traders", 125000.5))