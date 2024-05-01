class Product:

    def __init__(self, name, cost_price, description,expiry_date):
        self.name = name
        self.cost_price = cost_price
        self.description = description
        self.expiry_date = expiry_date

    def __repr__(self) -> str:
        
        return f'{self.name} {self.cost_price} {self.description}'
    
