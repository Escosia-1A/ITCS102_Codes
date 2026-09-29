# REVIEWER

age = int(input("Age: "))
rev = float(input("Revenue: "))
cc = int(input("Credit Score: "))
years = float(input("Years of Business: "))
has_defaults = bool(input("File of Bankruptcy -  "))
collateral = input("Collateral: ")
c_value = float(input("Value of Collateral: "))

max_loan = 0
base_fee = 0

if age >= 21 and has_defaults == False and years >= 2.0:
    print("BASELINE PASSED")
    if cc >= 720:
        print("CREDIT SCORE CONSIDERED HIGH")
        max_loan = rev * 3
        if rev >= 50000:
            print("ABOVE 50k REVENUE")
            base_fee = max_loan * 0.015
            print("BASE FEE IS SET TO ",base_fee)
        else:
            print("BELOW 50k REVENUE")
            base_fee = max_loan * 0.025
            print("BASE FEE IS SET TO ",base_fee)
    elif cc <= 620 and < 720:
        print("Credit Score is within range of 620 to 720")
        max_loan = rev * 1.5
        if years >= 5.0:
            base_fee + max_loan * 0.02
            print("Years in business greater than 5 years base fee is",base_fee)
        else
            base_fee + max_loan * 0.035
            print("Years in business lower than 5 years base fee is",base_fee)
        if c_value >= max_loan:
            print("COLLATERAL ",collateral," with a value of ",c_value, " is ACCEPTED")
        else:
            print("REJECTED: Insufficient collateral value for ", collateral, "")
    elif cc < 620:
        print("Credit Score too low")
    else:
        print("INVALID")
    else:
        print("CREDIT SCORE CONSIDERED LOW")
else:
    print("BASELINE FAILED")