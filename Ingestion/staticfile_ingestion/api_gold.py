# import json
# import csv
# from flatten_json import flatten
# import datetime

# # with open('coindesk_june_7_table.csv','r') as file_output:
# #     csv_reader=csv.DictReader(file_output)



# column_name = 'bpi_USD_rate_float'
# total = 0
# count = 0
# with open(f'coindesk_june_7_table.csv',mode ='r') as file_output:
#     csv_reader=csv.DictReader(file_output)
# for row in csv_reader:
#     value = row[column_name]
#     total += float(value)
#     count += 1

    
# if count > 0:
#     average = total / count
#     print(f"Average of {column_name}: {average}")
        
       
   
# # with open('coindesk_june_7_table.csv','a',newline='') as file:
# #     writer=csv.writer(file)
import json
import csv
from flatten_json import flatten
import datetime


file_path = 'coindesk_june_7_table.csv'
column_name = 'bpi_USD_rate_float'
total = 0
count = 0
with open(file_path,mode ='r') as file_output:
    csv_reader=csv.DictReader(file_output)
   # my_dict={}
    for row in csv_reader:
        value = row[column_name]
       # total += float(row[column_name])
        total += float(value)
        count += 1

    
if count > 0:
    average = total / count
    print(f"Average of {column_name}: {average}")
        #data_changed=my_dict.update(row)
    #my_dict=data_changed
    # data_gold= [dict(row) for row in csv_reader]
    #print(my_dict)
