# Store - retail
# warehouse stock management
# sales record
# staff information and Record
# Customer info
# products information

from typing import List


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
        cost = self.cost_price
        return f'{self.name}'



class Warehouse:
    # product info
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
        counter = {}
        for product in self.stock:
            if product.name in counter:
                counter[product.name] += 1
            else:
                counter[product.name] = 1

        
        if product_name == 'all':
            print(f'This is the quantity of all your products {counter}')


        if product_name in  counter: # yam ['yam', 'potato']
                print(f''' the total quantity of is {counter[product_name]}''')
        else:
            print(f'This product does not exist')

        # return f'You have no products to count'
    









#products
yam = Product(name= 'Yam', cost_price= 22.2,description= 'Ghanian Yam', expiry_date = '2001-01-01')    
yam2 = Product(name= 'Yam', cost_price= 22.2,description= 'Nigerian Yam', expiry_date = '2001-01-01')    
rice = Product('Rice', 25, 'Basmati', '2025-01-01')



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

for i in [rice, yam]:
    ware_house_texas.add_product(i)
# ware_house_texas.quantity() # all products
ware_house_texas.quantity('Yam') # give yam
ware_house_texas.quantity('Rice') # give yam

# remove 
# add 