#if application has high income and good credit.The person who applied is Eligible for loan

has_high_income = True
has_good_credit = False
has_low_income = False
has_bad_credit = True

if has_high_income and has_good_credit:
    print("Eligible For Loan")

elif has_low_income and has_bad_credit:
    print("Not Eligible For Loan")

elif has_high_income and has_bad_credit or has_low_income and has_good_credit:
    print("Not Eligible For Loan")
