from dataclasses import dataclass

# cash --> Bank
# capture sales
# Capture purchases
# Loan
# Investments


from typing import Any


# class BankInfo:
#     def __init__(self, name, branch):
#         self.name = name
#         self.branch = branch
#     def __str__(self):


@dataclass
class BankInfo:
    name: str
    branch: str 


class Bank:
    def __init__(self):
        self.bank_list = {} #boa #chase {'boa':{ balance: 0}
        
        # }}

    def register_bank(self, bank: BankInfo): #boa
        if bank not in self.bank_list:
            starting_balance = 0
            self.bank_list[bank.name] = {'balance': starting_balance}

    def deposit(self, amount, bank):
        
        self.bank_list[bank.name]['balance'] += amount




boa = BankInfo('Boa', 'Dallas')
llyold = BankInfo('Llyold', 'Dallas')

print(boa, llyold)



{'Boa':{ 'balance': 0},
 'chase': { 'balance': 0}}
