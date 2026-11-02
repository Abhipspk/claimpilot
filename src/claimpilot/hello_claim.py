import sys

def build_claim_line(claim_id,patient_id,procedure_code,amount):
    return f"{claim_id} | {patient_id} | {procedure_code} | RS {amount:,.2f}"

if __name__=="__main__":
    print(build_claim_line("CLM-0001","PAT-17","99213",1250.00))