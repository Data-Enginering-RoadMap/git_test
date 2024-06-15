
import requests
import json
#from datetime import datetime
import csv
from flatten_json import flatten

url = 'https://api.coindesk.com/v1/bpi/currentprice.json'

'https://www.alphavantage.co/'

response = requests.get(url)
# the move the api to a json file
data = response.json()
with open('output.json', 'w') as json_file:
    json.dump(data, json_file,indent =4)


# # convert json file to csv
# with open('output.json', 'r') as json_file:
#     data_2 = json.load(json_file)

# # if isinstance(data_2,dict):
# #     data_2[data_2]
# flat_data = [flatten(record)for record in data_2]
# keys = set()
# for record in flat_data:
#     keys.update(record.keys())
#     keys = list(keys)
# with open('coindeskoutput_csv.csv', 'w', newline = '') as csv_file:
#     writer = csv.DictWriter(csv_file, fieldnames = keys)
#     writer.writeheader()
#     writer.writerows(flat_data)
#print(response.json())
#GET
#POST
#PUT
