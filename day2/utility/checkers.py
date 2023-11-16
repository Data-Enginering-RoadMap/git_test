

def check_reversal(input, answer):
    if answer == '':
        return 
    try:
        assert answer == input[::-1]
        print("\033[92mPass: Reversal problem solved correctly.\033[0m")
    except:

        print(f"\033[91mFail: Reversal problem solution incorrect. Expected \"{input[::-1]}\" but got \"{answer}\".\033[0m")
     

def check_account_balance(inputed, answer):
    if answer == '':
        return 
    try:
        assert answer == deduct_amount(inputed)
        print("\033[92mPass: You have the correct list solved correctly.\033[0m")
    except:

        print(f"\033[91mFail: Reversal problem solution incorrect.\n  Expected::  \"{inputed}\" \n but got===> \n \n \"{answer}\".\033[0m")
     
def check_average_balance(inputed, answer):
    if answer == '':
        return 
    try:
        assert answer == calculate_average_balance(inputed)
        print("\033[92mPass: Congratulation!!! .\033[0m")
    except:

        print(f"\033[91mFail: Your answer is incorrect .\033[0m")
     



def deduct_amount(database):
    collections= []
    for account_type, products in database.items():
        for customers in products:
            for customer_key, customer_value in customers.items():
                    if customer_key =='age' and customer_value < 35:
                        current_balance = int(customers['account_balance'].replace('$', ''))
                        new_balance = current_balance - 200
                        result = {}
                        result['account_balance'] = f'${new_balance}' if new_balance >= 0 else '$0'
                        result['customer_name'] = customers['customer_name']
                        result['account_type'] = account_type
                        collections.append(result)
    return collections





def calculate_average_balance(database):
    account_types = ['savings_account', 'checking_account', 'investment_account', 'credit_card_account']
    balances = {}
    for account_type in account_types:
        customers = database.get(account_type, ())
        total_balance = 0
        count = 0
        
        for customer in customers:
            balance = int(customer['account_balance'])
            total_balance += balance
            count += 1
        
        if count > 0:
            average_balance = total_balance / count
            balances[account_type]= average_balance
        else:
            print(f"No customers found for {account_type}")
    return balances

# Call the function with the provided Database

