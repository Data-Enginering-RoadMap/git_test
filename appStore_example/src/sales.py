

# identify products --- # Warehouse
# which employee sold
# customer details
# interact cash systerm




class Sales:

    def __init__(self, warehouse, bank):
        self.warehouse = warehouse
        self.bank = bank

    def __str__(self) -> str:
        pass


    def sales(self, product, quantity, price):
        product_price = self.warehouse.price(product)

        if price < product_price :
            raise Exception('invalid')
        
        print(self.warehouse.quantity(product))
        self.warehouse.remove_product(product, quantity)
        print(self.warehouse.quantity(product))

        total_price = price * quantity

        self.bank.deposit(total_price, 'Boa')

        #

