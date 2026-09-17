# [COMP-1327 Assignment 2]

## Description

The program is intended to help new or existing customers choose which type of chequing account they should choose at Pixel River Financial(PRF) bank. To achieve this purpose, the user will be prompted many questions.

## Author

Jeremy Fuentes Rivera Ramirez

## Account Type Test Cases

# ***Tested Case 1***

# Test Values:
    - age: 59 and 61

# Variables used for testing:
    - "age" and "is_student"

# Expected Result:
    - First output:"Are you a student? Type 'y' for yes or 'n' for no: "
    - Second output: Nothing gets printed

# Actual Result:
    - First output:"Are you a student? Type 'y' for yes or 'n' for no: "
    - Second output: Nothing gets printed

# ***Tested Case 2***

# Test Values:
    - monthly_transactions: 2 and 12

# Variables used for testing:
    - "monthly_transaction" and "account_type"

# Expected Result:
    - First output:
    "
    ----------------------------------------
    Recommended Account: Basic Account"

    - Second output: 
    "
    ----------------------------------------
    Recommended Account: Basic Account"

# Actual Result:
    - First output:
    "
    ----------------------------------------
    Recommended Account: Basic Account"

    Second output: 
    "
    ----------------------------------------
    Recommended Account: Basic Account"

# ***Tested Case 3***

# Test Values:
    - monthly_transaction: 17 and 25

# Variables used for testing:
    - "monthly_transaction" and "account_type"

# Expected Result:
    - First output:
    "
    ----------------------------------------
    Recommended Account: Basic Plus Account"

    - Second output: 
    "
    ----------------------------------------
    Recommended Account: Basic Plus Account"

# Actual Result:
    - First output:
    "
    ----------------------------------------
    Recommended Account: Basic Plus Account"

    - Second output: 
    "
    ----------------------------------------
    Recommended Account: Basic Plus Account"

# ***Tested Case 4***

# Test Values:
    - monthly_transaction: 40
    - is_prf_abm_user: 'n'
    - is_e_transfer_sender: 'n'

# Variables used for testing:
    - "account_type", "monthly_transaction", "is_prf_abm_user" and "is_e_transfer_sender"

# Expected Result:
    - First output:
    "
    ----------------------------------------
    Recommended Account: Preferred Account"

    - Second output: 
    "
    ----------------------------------------
    Recommended Account: Preferred Account"

# Actual Result:
    - First output:
    "
    ----------------------------------------
    Recommended Account: Preferred Account"

    - Second output: 
    "
    ----------------------------------------
    Recommended Account: Preferred Account"

# ***Tested Case 5***

# Test Values:
    - monthly_transaction: 45
    - is_prf_abm_user: 'y'
    - is_e_transfer_sender: 'y'

# Variables used for testing:
    - "account_type", "monthly_transaction", "is_prf_abm_user" and "is_e_transfer_sender"

# Expected Result:
    - First output:
    "
    ----------------------------------------
    Recommended Account: Ultimate Account"

    - Second output: 
    "
    ----------------------------------------
    Recommended Account: Ultimate Account"

# Actual Result:
    - First output:
    "
    ----------------------------------------
    Recommended Account: Ultimate Account"

    - Second output: 
    "
    ----------------------------------------
    Recommended Account: Ultimate Account"

# ***Tested Case 6***

# Test Values
    - monthly_transaction: 50
    - is_prf_abm_user: 'y'
    - is_e_transfer_sender: 'n'

# Variables used for testing:
    - "account_type", "monthly_transaction", "is_prf_abm_user" and "is_e_transfer_sender"

# Expected Result:
    - First output:
    "
    ----------------------------------------
    Recommended Account: Ultimate Account"

    - Second output: 
    "
    ----------------------------------------
    Recommended Account: Ultimate Account"

# Actual Result:
    - First output:
    "
    ----------------------------------------
    Recommended Account: Ultimate Account"

    - Second output: 
    "
    ----------------------------------------
    Recommended Account: Ultimate Account"

# ***Tested Case 7***
# Test Values
    - monthly_transaction: 59
    - is_prf_abm_user: 'n'
    - is_e_transfer_sender: 'y'

# Variables used for testing:
    - "account_type", "monthly_transaction", "is_prf_abm_user" and "is_e_transfer_sender"

# Expected Result:
    - First output:
    "
    ----------------------------------------
    Recommended Account: Ultimate Account"

    - Second output: 
    "
    ----------------------------------------
    Recommended Account: Ultimate Account"

# Actual Result:
    - First output:
    "
    ----------------------------------------
    Recommended Account: Ultimate Account"

    - Second output: 
    "
    ----------------------------------------
    Recommended Account: Ultimate Account"

## Monthly Fee Test Cases

# ***Tested Case 8***

# Test Values:
    - age: 59 
    - is_student: 'y'
    - monthly_transaction: 11

# Variables used for testing:
    - "age", "is_student", "monthly_transaction", "account_type" and "fee"

# Expected Result:
    - Output:
    "
    ----------------------------------------
    Recommended account: Basic Account
    Monthly fee: $1.98"

# Actual Result:
    - Output:
    "
    ----------------------------------------
    Recommended account: Basic Account
    Monthly fee: $1.98"

# ***Tested Case 9***

# Test Values:
    - age: 30
    - is_student: 'n'
    - monthly_transaction: 8

# Variables used for testing:
    - "age", "is_student", "monthly_transaction", "account_type" and "fee"

# Expected Result:
    - Output:
    "
    ----------------------------------------
    Recommended account: Basic Account
    Monthly fee: $3.95"

# Actual Result:
    - Output:
    "
    ----------------------------------------
    Recommended account: Basic Account
    Monthly fee: $3.95" 

# ***Tested Case 10***

# Test Values:
    - age: 60
    - monthly_transaction: 9

# Variables used for testing:
    - "age", "is_student", "monthly_transaction", "account_type" and "fee"

# Expected Result:
    - Output:
   "
    ----------------------------------------
    Recommended account: Basic Account
    Monthly fee: $0.00"

# Actual Result:
    - Output:
   "
    ----------------------------------------
    Recommended account: Basic Account
    Monthly fee: $0.00" 

# ***Tested Case 11***

# Test Values:
    - monthly_transaction: 24 
    - avg_monthly_balance: 3000

# Variables used for testing:
    - "age", "is_student", "monthly_transaction", "account_type" and "fee"

# Expected Result:
    - Output:
   "
    ----------------------------------------
    Recommended account: Basic Plus Account
    Monthly fee: $0.00"

# Actual Result:
    - Output:
    "
    ----------------------------------------
    Recommended account: Basic Plus Account
    Monthly fee: $0.00"

# ***Tested Case 12***

# Test Values:
    - avg_monthly_balance: 1000
    - age: 14
    - is_student: 'y'
    - monthly_transactions: 23

# Variables used for testing:
    - "age", "is_student", "monthly_transaction", "account_type" and "fee"

# Expected Result:
    - Output:
   "
    ----------------------------------------
    Recommended account: Basic Plus Account
    Monthly fee: $5.97"

# Actual Result:
    - Output:
    "
    ----------------------------------------
    Recommended account: Basic Plus Account
    Monthly fee: $5.97"

# ***Tested Case 13***

# Test Values:
    - monthly_transaction: 20
    - avg_monthly_balance: 2000
    - age: 57
    - is_student: 'n'

# Variables used for testing:
    - "age", "is_student", "monthly_transaction", "account_type" and "fee"

# Expected Result:
    - Output:
   "
    ----------------------------------------
    Recommended account: Basic Plus Account
    Monthly fee: $11.95"

# Actual Result:
    - Output:
    "
    ----------------------------------------
    Recommended account: Basic Plus Account
    Monthly fee: $11.95"

# ***Tested Case 14***

# Test Values:
    - monthly_transaction: 21
    - avg_monthly_balance: 2000
    - age: 80

# Variables used for testing:
    - "age", "is_student", "monthly_transaction", "account_type" and "fee"

# Expected Result:
    - Output:
   "
    ----------------------------------------
    Recommended account: Basic Plus Account
    Monthly fee: $8.37"

# Actual Result:
    - Output:
    "
    ----------------------------------------
    Recommended account: Basic Plus Account
    Monthly fee: $8.37"

# ***Tested Case 15***

# Test Values:
    - monthly_transaction: 28
    - is_prf_abm_user: 'n'
    - is_e_transfer_sender: 'n'
    - avg_monthly_balance: 4000

# Variables used for testing:
    - "age", "is_student", "monthly_transaction", "account_type", "is_prf_abm_user", "is_e_transfer_sender" and "fee"

# Expected Result:
    - Output:
   "
    ----------------------------------------
    Recommended account: Preferred Account
    Monthly fee: $0.00"

# Actual Result:
    - Output:
    "
    ----------------------------------------
    Recommended account: Preferred Account
    Monthly fee: $0.00"

# ***Tested Case 16***

# Test Values:
    - monthly_transaction: 30
    - is_prf_abm_user: 'n'
    - is_e_transfer_sender: 'n'
    - avg_monthly_balance: 3000
    - age: 40
    - student: 'y'

# Variables used for testing:
    - "age", "is_student", "monthly_transaction", "account_type", "is_prf_abm_user", "is_e_transfer_sender" and "fee"

# Expected Result:
    - Output:
   "
    ----------------------------------------
    Recommended account: Preferred Account
    Monthly fee: $8.47"

# Actual Result:
    - Output:
    "
    ----------------------------------------
    Recommended account: Preferred Account
    Monthly fee: $8.47"

# ***Tested Case 17***

# Test Values:
    - monthly_transaction: 32
    - is_prf_abm_user: 'n'
    - is_e_transfer_sender: 'n'
    - avg_monthly_balance: 2000
    - age: 14
    - student: 'n'

# Variables used for testing:
    - "age", "is_student", "monthly_transaction", "account_type", "is_prf_abm_user", "is_e_transfer_sender" and "fee"

# Expected Result:
    - Output:
   "
    ----------------------------------------
    Recommended account: Preferred Account
    Monthly fee: $16.95"

# Actual Result:
    - Output:
    "
    ----------------------------------------
    Recommended account: Preferred Account
    Monthly fee: $16.95"

# ***Tested Case 18***

# Test Values:
    - monthly_transaction: 28
    - is_prf_abm_user: 'n'
    - is_e_transfer_sender: 'n'
    - avg_monthly_balance: 1000
    - age: 80

# Variables used for testing:
    - "age", "is_student", "monthly_transaction", "account_type", "is_prf_abm_user", "is_e_transfer_sender" and "fee"

# Expected Result:
    - Output:
   "
    ----------------------------------------
    Recommended account: Preferred Account
    Monthly fee: $11.86"

# Actual Result:
    - Output:
    "
    ----------------------------------------
    Recommended account: Preferred Account
    Monthly fee: $11.86"

# ***Tested Case 20***

# Test Values:
    - monthly_transaction: 30
    - is_prf_abm_user and is_e_transfer_sender: ('y', 'n'; 'y', 'y'; 'n', 'y')
    - avg_monthly_balance: 6000

# Variables used for testing:
    - "age", "is_student", "monthly_transaction", "account_type", "is_prf_abm_user", "is_e_transfer_sender", avg_monthly_balance and "fee"

# Expected Result:
    - Output:
    "
    ----------------------------------------
    Recommended account: Ultimate Account
    Monthly fee: $0.00

# Actual Result:
    - Output:
    "
    ----------------------------------------
    Recommended account: Ultimate Account
    Monthly fee: $0.00"

# ***Tested Case 21***

# Test Values:
    - monthly_transaction: 35
    - is_prf_abm_user and is_e_transfer_sender: ('y', 'n'; 'y', 'y'; 'n', 'y')
    - avg_monthly_balance: 3000
    - age: 30
    - student: 'y'

# Variables used for testing:
    - "age", "is_student", "monthly_transaction", "account_type", "is_prf_abm_user", "is_e_transfer_sender", avg_monthly_balance and "fee"

# Expected Result:
    - Output:
    "
    ----------------------------------------
    Recommended account: Ultimate Account
    Monthly fee: $15.47"

# Actual Result:
    - Output:
    "
    ----------------------------------------
    Recommended account: Ultimate Account
    Monthly fee: $15.47"

# ***Tested Case 22***

# Test Values:
    - monthly_transaction: 40
    - is_prf_abm_user and is_e_transfer_sender: ('y', 'n'; 'y', 'y'; 'n', 'y')
    - avg_monthly_balance: 2000
    - age: 14
    - student: 'n'

# Variables used for testing:
    - "age", "is_student", "monthly_transaction", "account_type", "is_prf_abm_user", "is_e_transfer_sender", avg_monthly_balance and "fee"

# Expected Result:
    - Output:
    "
    ----------------------------------------
    Recommended account: Ultimate Account
    Monthly fee: $30.95"

# Actual Result:
    - Output:
    "
    ----------------------------------------
    Recommended account: Ultimate Account
    Monthly fee: $30.95"

# ***Tested Case 23***

# Test Values:
    - monthly_transaction: 45
    - is_prf_abm_user and is_e_transfer_sender: ('y', 'n'; 'y', 'y'; 'n', 'y')
    - avg_monthly_balance: 1000
    - age: 90

# Variables used for testing:
    - "age", "is_student", "monthly_transaction", "account_type", "is_prf_abm_user", "is_e_transfer_sender", avg_monthly_balance and "fee"

# Expected Result:
    - Output:
    "
    ----------------------------------------
    Recommended account: Ultimate Account
    Monthly fee: $21.66"

# Actual Result:
    - Output:
    "    
    ----------------------------------------
    Recommended account: Ultimate Account
    Monthly fee: $21.66"