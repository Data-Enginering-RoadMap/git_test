import json
import csv
from flatten_json import flatten
import datetime
#flatten json file
coindesk_june_7_flat='coindesk_june_7.json'
# flat_file= ('coindesk_june_7.json')
# def flatten_dict(d, parent_key='', sep=','):
#     # items = []
#     # for k, v in d.items():
#     #     new_key = f"{parent_key}{sep}{k}" if parent_key else k
#     #     if isinstance(v, dict):
#     #         items.extend(flatten_dict(v, new_key, sep=sep).items())
#     #     else:
#     #         items.append((new_key, v))
#     # return dict(items)

# Example usage:
#nested_dict = {'key1': {'key2': 'value2', 'key3': 'value3'}, 'key4': 'value4'}
# flat_dict = flatten_dict(flat_file)
# print(flat_dict)

#read json file
with open(coindesk_june_7_flat) as file:
    data_trans=json.load(file)
    data_trans=flatten(data_trans) 
    current_date=datetime.datetime.now()
    # for row in data_trans:
    #    row['ETL_time']=current_date.strftime('%Y-%M-%D %H:%M:%S')
    data_trans['ETL_time'] = current_date.strftime('%Y-%M-%D %H:%M:%S')
    
   


    
        

    # with open('coindesk_june_7_table.csv','w',newline='') as file_trans:
    #     file_trans.write(str(data_trans))
with open('coindesk_june_7_table.csv','r') as file_trans:
    file_read_attempt=file_trans.read()
print(file_read_attempt)
#open a csv file for writing
with open('coindesk_june_7_table.csv','w',newline='') as file:
    writer=csv.writer(file)
#write headers to csv
    headers=data_trans.keys()
    writer.writerow(headers)
    body=data_trans.values()
    writer.writerow(body)
with open('coindesk_june_7_table.csv','r') as file_output:
    file_read_attempt=file_output.read()
    print(file_read_attempt)
    print (type(file_read_attempt))