# 1. Obtaining Customer Information
age = int(input("Enter your age: "))

is_student = False # Setting a value to avoid not having a value assigned.
if age < 60:
    is_student = (input("Are you a student? Type 'y' for yes or 'n' for no: ")) == "y"

print("")
monthly_transactions = int(input("Indicate the number of transactions you do per month: "))
is_prf_abm_user = (input("Do you bank at non-PRF Automatic Banking Machines(ABM)? Type 'y' for yes or 'n' for no: "))  == "y"
is_e_transfer_sender = (input("Do you send e-transfer? Type 'y' for yes or 'n' for no: ")) == "y"
avg_monthly_balance = float(input("Please indicate the average amount of money you have in your account each month: "))

# 2. Determining the Account Type
account_type = "undetermined" # Setting this value to a specific one for testing purposes.
if (monthly_transactions <= 12):
    account_type = "Basic"  
elif (monthly_transactions <= 25):
    account_type = "Basic Plus"
else:
    if ((not is_prf_abm_user) and (not is_e_transfer_sender)):
        account_type = "Preferred"
    else:
        account_type = "Ultimate"

print("")
print("-" * 40)
print(f"Recommended account: {account_type} Account")

# 3. Determining the Monthly Fee
if account_type == "Basic":
    fee = 3.95 # Default value given to avoid redundancy
    if (not is_student):
        if age  >= 60:
            fee = 0.00 # waived fee
    else:
        fee -= (fee * (0.50)) # 50% discount applied.
elif account_type == "Basic Plus":
    fee = 11.95 # Default value given to avoid redundancy
    if avg_monthly_balance >= 3000:
        fee = 0.00 # waived fee
    else:
        if (not is_student):
            if age  >= 60:
                fee -= (fee * (0.30)) # 30% discount applied.
        else:
            fee -= (fee * (0.50)) # 50% discount applied.
elif account_type == "Preferred":
    fee = 16.95 # Default value given to avoid redundancy
    if avg_monthly_balance >= 4000:
        fee = 0.00 # waived fee
    else:
        if (not is_student):
            if age  >= 60:
                fee -= (fee * (0.30)) # 30% discount applied.
        else:
            fee -= (fee * (0.50)) # 50% discount applied.
else:
    fee = 30.95 # Default value given to avoid redundancy
    if avg_monthly_balance >= 6000:
        fee = 0.00 # waived fee
    else:
        if (not is_student):
            if age  >= 60:
                fee -= (fee * (0.30)) # 30% discount applied.
        else:
            fee -= (fee * (0.50)) # 50% discount applied.

fee = round(fee, 2)
print(f"Monthly fee: ${fee:.2f}")