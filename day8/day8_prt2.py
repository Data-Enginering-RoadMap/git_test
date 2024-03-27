class Animal: #Object
   # attributes
    legs = True
    mouth = True
    eyes = True

   # methods
    def move(self):
        return True
    
    @property
    def run(self):
        return True

class Dog(Animal): 
    speak = 'Bark'

class Cat(Animal):
    speak = 'Meow'

import random

sally = Dog()# instantiating a class
Billy = Dog()# instantiating a class
Bella = Dog()# instantiating a class
Bingo = Dog()# instantiating a class

print(Bingo.run, Bingo.move())

# df_salar = pd.read_csv(xxxxxxxx)
# df_employee = pd.read_csv(xxxxxxxx)

# df_salar.merge
# df_employee.merge

# df.head() --> method
# df.dtypes --> attribute



class Bank:

    investment_type =['checking', 'savings']
    customer = {}

    def __init__(self, name):
        self.name = name

    def open_account(self, name, addr, age):
        self.customer[name]= {'address': addr, 'age': age}
        # # no = len(self.customer.keys)
        # no += 1
        # self.customer[name]['account_no'] = no
    def deposit(self, customer_name, amount):
        customer = self.customer.get(customer_name)
        customer = self.customer.get(customer_name)
        customer = self.customer.get(customer_name)
        customer = self.customer.get(customer_name)
        customer = self.customer.get(customer_name)
        return customer

    def __str__(self):
        return f'This Bank has {self.name} and has the following customers {self.customer}'



class CitiBank(Bank):
    
    def __str__(self):
        return f'This Bank has my custom Bank for Citi'
    

    def deposit(self, customer_name, amount):
        # ans = super().deposit(customer_name, amount)
        
        # return ans, 'new answer'





Citi= CitiBank('Citi')
BOA= Bank('BOA')
Chase= Bank('Chase')
print(Chase)
print(Citi)
print(BOA)

Citi.open_account('Ade','112 tx', 10)
BOA.open_account('Ade','112 tx', 10)
Chase.open_account('Ade','112 tx', 10)
print(Chase)
print(Citi)
print(BOA)

print(Citi.deposit('Ade', '100'))
print(BOA.deposit('Ade', '5000'))
print(Chase.deposit('Ade', '200'))





