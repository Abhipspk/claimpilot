class Claim:
    def __init__(self,claim_id, patient_id, provider_id, procedure_code, amount):
        self.claim_id = claim_id
        self.patient_id = patient_id
        self.provider_id = provider_id
        self.procedure_code = procedure_code
        self.amount = amount

    def summary(self):
        return f"{self.claim_id} | {self.patient_id} | {self.provider_id} | {self.procedure_code} | (Rs: {self.amount:,.2f})"

if __name__ == "__main__":
    c1 = Claim("CLM-0001", "PAT-17", "PR001", "99123", 1250.00)
    c2 = Claim("CLM-0005", "PAT-25", "PR005", "10957", 1800.00)
    print(c1.summary())
    c1.amount=1600
    print(c1.summary())
    print(Claim)
    print(c1 == Claim("CLM-0001", "PAT-17", "PR001", "99123", 1600))