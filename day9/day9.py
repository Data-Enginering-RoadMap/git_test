# Store - retail
# warehouse stock management
# sales record
# staff information and Record
# Customer info
# products information

from typing import List
from collections import Counter, namedtuple

class Store:
    name: str = 'Ola Afrik store'
    location = 'Dubai'


class Product:

    def __init__(self, name, cost_price, description,expiry_date):
        self.name = name
        self.cost_price = cost_price
        self.description = description
        self.expiry_date = expiry_date

    def __repr__(self) -> str:
        
        return f'{self.name} {self.cost_price} {self.description}'
    

#dunder === . double underscore

class Warehouse:

    def __init__(self, stock: List[Product]) -> None:
        self.stock = stock

    def add_product(self, product: Product):
        self.stock.append(product)
        
    def __repr__(self) -> str:
        if type(self.stock) != list:
            raise  Exception('wrong container')
        #total number
        return f'You currently have a total of {len(self.stock)} products in your warehouse'
        
    def quantity(self, product_name='all'):

        # counter = {}
        # for product in self.stock:
        #     if product.name in counter:
        #         counter[product.name] += 1
        #     else:
        #         counter[product.name] = 1

        #pythonic way
        counter = Counter([product.name for product in self.stock ])


        
        if product_name == 'all':
            print(f" {'-'* (len('ProductName')+4):>20} {'-'* (len('Quantity')+4): >20}  ")
            print(f" {'| '+'ProductName'+' |': >20} {'| '+'Quantity'+' |': >20}")
            print(f" {'-'* (len('ProductName')+4):>20} {'-'* (len('Quantity')+4): >20}  ")
            for key, value in counter.items():
                print(f" {key: >20} {value: >20}")
            else:
                print('\n', end='\n')
                

        if product_name in  counter: # yam ['yam', 'potato']
            print(f" {'-'* (len('ProductName')+4):>20} {'-'* (len('Quantity')+4): >20}  ")
            print(f" {'| '+'ProductName'+' |': >20} {'| '+'Quantity'+' |': >20}")
            print(f" {'-'* (len('ProductName')+4):>20} {'-'* (len('Quantity')+4): >20}  ")
            print(f" {product_name: >20} {counter[product_name]: >20}")
            print('\n', end='\n')
                
    
    def remove_product(self, product_name, quantity):
        count = 0
        i= 0
        while i < len(self.stock) and count < quantity:
            if self.stock[i].name.lower() == product_name.lower():
                del self.stock[i]
                count += 1
            else:
                i += 1
        
        # self.quantity()



class EmployeeRecord:

    def __init__(self, employee):
        self.employees = employee

    def add_employee(self, employee):
        if type(employee) == set:
            self.employees = self.employees.union(employee)
        else:
            try:
                self.employees.add(employee)
            except:
                print('You have inputted the wrong value')

    def print_employee(self):
        print(f" {'Staff ID': >10s} {'StaffName': >10s}")
        for indx, staff in enumerate(self.employees):
            print(f" {indx: >10d} {staff.Name: >10s}")




info = ['Name', 'Age', 'address', 'phn_no','next_of_kin']
staff = namedtuple('staff', info )


ade = staff('ade', 10, 'dallas','123432', 'bob')
sam = staff('sam', 10, 'dallas','123432', 'bob')
shaun = staff('shaun', 10, 'dallas','123432', 'bob')
mike = staff('mike', 10, 'dallas','123432', 'bob')
Vik = staff('Vik', 10, 'dallas','123432', 'bob')

# NewAmEmpRecord = EmployeeRecord(set())

# NewAmEmpRecord.add_employee(ade)
# NewAmEmpRecord.add_employee({sam, shaun, Vik, mike, Vik})
# NewAmEmpRecord.add_employee(ade)
# NewAmEmpRecord.print_employee()

#         # return f'You have no products to count'
    




if __name__ == '__main__':

    #products
    yam = Product(name= 'Yam', cost_price= 22.2,description= 'Ghanian Yam', expiry_date = '2001-01-01')    
    yam2 = Product(name= 'Yam', cost_price= 22.2,description= 'Nigerian Yam', expiry_date = '2001-01-01')    
    rice = Product('Rice', 25, 'Basmati', '2025-01-01')
    bean = Product('Bean', 10, 'Agoyin', '2025-01-01')
    potato = Product('Potatoe', 25, 'Irish', '2025-01-01')
    potato2 = Product('Potatoe', 25, 'Sweet', '2025-01-01')



    ware_house_Dc= Warehouse(stock = [yam, yam2, yam])
    ware_house_texas= Warehouse(stock = [])

    ware_house_Dc
    ware_house_texas

    #2days after we restocked our warehouse
    # ware_house_texas.add_product(yam)
    # ware_house_texas.add_product(yam2)
    # ware_house_texas.add_product(rice)
    # ware_house_texas.add_product(rice)
    # ware_house_texas.add_product(rice)
    # ware_house_texas.add_product(rice)
    # ware_house_texas.add_product(rice)
    # ware_house_texas.add_product(rice)
    # ware_house_texas.add_product(rice)
    # ware_house_texas.add_product(rice)
    # ware_house_texas.add_product(rice)

    list_of_product = [rice, yam, rice, yam, rice , 
                    rice, rice, yam, rice, yam2,
                    potato, potato2, bean, bean,
                    yam, potato, bean, bean

                    
                    ]

    for item in list_of_product:
        ware_house_texas.add_product(item)

    for i in [rice, yam]:
        ware_house_texas.add_product(i)

    ware_house_texas.quantity() # give yam
    ware_house_texas.quantity('Rice') # give yam


    ware_house_texas.remove_product('Bean',1)
    ware_house_texas.remove_product('Bean',1)
    ware_house_texas.remove_product('rice',2)
    ware_house_texas.remove_product('bean',2)

    # ware_house_texas.quantity() # give yam
    NewAmEmpRecord = EmployeeRecord(set())

    NewAmEmpRecord.add_employee(ade)
    NewAmEmpRecord.add_employee({sam, shaun, Vik, mike, Vik})
    NewAmEmpRecord.add_employee(ade)
    NewAmEmpRecord.print_employee()

# 

# remove 
# add 