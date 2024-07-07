
from src.cash import Bank
from src.employee import EmployeeRecord
from src.warehouse import Warehouse
from src.products import Product
from src.sales import Sales

from collections import namedtuple

info = ['Name', 'Age', 'address', 'phn_no','next_of_kin']
staff = namedtuple('staff', info )


ade = staff('ade', 10, 'dallas','123432', 'bob')
sam = staff('sam', 10, 'dallas','123432', 'bob')
shaun = staff('shaun', 10, 'dallas','123432', 'bob')
mike = staff('mike', 10, 'dallas','123432', 'bob')
Vik = staff('Vik', 10, 'dallas','123432', 'bob')





#products
yam = Product(name= 'Yam', cost_price= 22.2,description= 'Ghanian Yam', expiry_date = '2001-01-01')    
yam2 = Product(name= 'Yam', cost_price= 22.2,description= 'Nigerian Yam', expiry_date = '2001-01-01')    
rice = Product('Rice', 25, 'Basmati', '2025-01-01')
bean = Product('Bean', 10, 'Agoyin', '2025-01-01')
potato = Product('Potatoe', 25, 'Irish', '2025-01-01')
potato2 = Product('Potatoe', 25, 'Sweet', '2025-01-01')



ware_house_Dc= Warehouse([])

for i in [ yam, yam2, rice, bean, rice, rice]:
    ware_house_Dc.add_product(i)

ware_house_Dc


sales = Sales(ware_house_Dc)

sales.sales('Rice', 1)