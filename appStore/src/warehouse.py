from typing import List
from collections import namedtuple, Counter
from products import Product




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