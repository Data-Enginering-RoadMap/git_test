import json
import csv
from flatten_json import flatten
import datetime
from collections import defaultdict
from pprint import pprint


# read silver table for the exact day
# check gold table for existing record

# day 1
# ingestion 1 silver 1 gold 1

# day 2
# ingestion 2 silver 2 gold 1

#read gold
#add todays silver with GOlds record  then aggregate
#

dictionary= defaultdict(list)

def read_silver(file_path):
    global dictionary
    with open(file_path,'r') as f:
            
            csv_reader= f.readlines()
            for indx, i in enumerate(csv_reader):

                item = i.split('|')
                item = [ x.strip() for x in item]

                if indx == 0: # the header will always be 0
                    header = item 
                else:
                    body = item
                    for key, value in zip(header, body):
                         dictionary[key].append(value)
                # item = dict(zip(header,body))

    return dictionary


def get_gold():
     with open('api_project/Storage/Gold/data_gold.txt', 'r') f:
        data = f.read()
        if data:
             return data
        else: 
            return None



def culave(file_path):
     # value from silver
    silver = read_silver(file_path)
    av_float = silver['bpi_GBP_rate_float']
     #value from gold

    gold= get_gold()
    if gold == None:
          # no data
        # write silver data
        with open('gold_path', w) as f:
            #header 
            f.write(f'{av_float}, 1' )# data


        pass


        
def gold(file_path):
    # reading silver file

    culave(file_path)
            
        
    pprint(dictionary)
    # write your gold logic here                





# def cal_col_avg(file_path, column_name):
# #file_path = 'coindesk_june_7_table.csv'
# #column_name = 'bpi_USD_rate_float'
#     total = 0
#     count = 0
#     try:
#         with open(file_path, mode = 'r') as file_output:
# #with open(file_path,mode ='r') as file_output:
#             csv_reader=csv.DictReader(file_output)
#             for row in csv_reader:
#                 value = row[column_name]
#                  try:
#    # my_dict={}
#     #for row in csv_reader:
#        # value = row[column_name]
#        # total += float(row[column_name])
#                     total += float(value)
#                     count += 1

    
# if count > 0:
#     average = total / count
#     print(f"Average of {column_name}: {average}")
#         #data_changed=my_dict.update(row)
#     #my_dict=data_changed
#     # data_gold= [dict(row) for row in csv_reader]
#     #print(my_dict)