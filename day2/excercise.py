from utility.checkers import *

# SECTION A
# write a loop that will reverse every string 

input_item= 'zzubzzif'
#put your code here




input_ans = ''  # store your anser here
check_reversal(input_item,input_ans)


# SECTION B
# You own a deposit money Bank. 
# Your bank stores customers information in the following way

Database = {
    'savings_account': (
        {
            'customer_name': 'John Smith',
            'account_balance': '5000',
            'year_opened': 2020,
            'age': 35,
            'Active': True,
            'card': 'active',
        },
        {
            'customer_name': 'Emma Johnson',
            'account_balance': '3200',
            'year_opened': 2021,
            'age': 28,
            'Active': False,
            'card': 'not active',
        },
        # Add more customers for savings_account
        {
            'customer_name': 'Liam Davis',
            'account_balance': '2800',
            'year_opened': 2019,
            'age': 31,
            'Active': True,
            'card': 'active',
        },
        {
            'customer_name': 'Sophie Wilson',
            'account_balance': '4100',
            'year_opened': 2023,
            'age': 29,
            'Active': True,
            'card': 'not active',
        },
        {
            'customer_name': 'Noah Taylor',
            'account_balance': '4500',
            'year_opened': 2020,
            'age': 27,
            'Active': True,
            'card': 'active',
        },
        {
            'customer_name': 'Olivia Moore',
            'account_balance': '3800',
            'year_opened': 2022,
            'age': 33,
            'Active': False,
            'card': 'not active',
        },
    ),
    'checking_account': (
        {
            'customer_name': 'Michael Brown',
            'account_balance': '2500',
            'year_opened': 2019,
            'age': 40,
            'Active': True,
            'card': 'active',
        },
        {
            'customer_name': 'Sophia Rodriguez',
            'account_balance': '4000',
            'year_opened': 2022,
            'age': 32,
            'Active': True,
            'card': 'not active',
        },
    ),
    'investment_account': (
        
        {
            'customer_name': 'William Lee',
            'account_balance': '10000',
            'year_opened': 2018,
            'age': 45,
            'Active': False,
            'card': 'not active',
        },
        {
            'customer_name': 'Olivia Kim',
            'account_balance': '8000',
            'year_opened': 2020,
            'age': 30,
            'Active': True,
            'card': 'active',
        },

    ),
    'credit_card_account': (
        {
            'customer_name': 'Daniel Chen',
            'account_balance': '1500',
            'year_opened': 2023,
            'age': 26,
            'Active': True,
            'card': 'active',
        },
        {
            'customer_name': 'Ava Williams',
            'account_balance': '2000',
            'year_opened': 2022,
            'age': 29,
            'Active': False,
            'card': 'not active',
        },
    ),
}



''' Question 1
 if a customer is less than 35years deduct 200 from each value adn return their name, balance and account_type
 your result should look like [{account_balance: xxxx, customer_name: xxxx, account_type: xxxxx }]
'''
#your code here



account_balance_53 = '' # put your answer here




check_account_balance(Database, account_balance_53)

""" Question 2
Average Account Balance:
Calculate and display the average account balance for each account type ('savings_account', 'checking_account', 'investment_account', 'credit_card_account').
"""
#your code here






average_balance = "" # put your answer here
check_average_balance(Database, average_balance)

#Extras

# Oldest Customer:
# Determine the name of the oldest customer among all account types.

# Inactive Accounts:
# Identify and display the number of inactive accounts for each account type.

# Young Active Customers:
# List the names of customers below the age of 30 who have an active account status.
