
import requests
import json
import csv

url = 'https://api.coindesk.com/v1/bpi/currentprice.json'

#'https://www.alphavantage.co/'

response = requests.get(url)
#print(type(response.json()))
data = response.json()
with open('coindesk_june_7.json', 'w') as file:
    json.dump(data, file,indent=4) 

#read json file
# with open('coindesk_june_7.json') as file:
#     data_trans=json.load(file) 
# #open a csv file for writing
# with open('coindesk_june_7_table.csv','w',newline='') as file:
#     writer=csv.writer(file)
# #write headers to csv
#     headers=data_trans[0].keys()
#     writer.writerow(headers)
#     for item in data_trans:
#         writer.writerow(item.values())

#GET
#POST
#PUT
