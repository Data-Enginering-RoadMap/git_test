import json
import csv
from flatten_json import flatten
import datetime

def cal_col_avg(file_path, column_name):
#file_path = 'coindesk_june_7_table.csv'
#column_name = 'bpi_USD_rate_float'
    total = 0
    count = 0
    try:
        with open(file_path, mode = 'r') as file_output:
#with open(file_path,mode ='r') as file_output:
            csv_reader=csv.DictReader(file_output)
            for row in csv_reader:
                value = row[column_name]
                 try:
   # my_dict={}
    #for row in csv_reader:
       # value = row[column_name]
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