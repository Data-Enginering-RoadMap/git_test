import json
import csv
from flatten_json import flatten
import datetime
from collections import defaultdict
from pprint import pprint
import statistics
from transformation.api_silver import file_opener
from pathlib import Path

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

gold_storage_location='api_project/Storage/Gold'
gold_file='api_project/Storage/Gold/data_gold.csv'
def get_gold():
    path=Path(gold_storage_location)
    #path=Path('api_project/Storage/Gold')
    if path.exists():
        with open(gold_file, 'r') as f:
            data = f.read()
            if data:
                return data
    path.mkdir()
    return None
# def write_csv(file_location, mode,data,**kwargs):
#     f = file_opener(file_location, mode,**kwargs)
#     writer=csv.writer(f)
#     writer.writerows(data)
        
time_loaded=datetime.datetime.now().strftime('%Y-%M-%D %H:%M:%S')

def culave(file_path,file_opener):
     # value from silver
    silver = read_silver(file_path)
    av_float = silver['bpi_GBP_rate_float']
    av_float=av_float[0]
    gold_data= " "
    print(av_float)
    print (gold_data)

     #value from gold

    gold= get_gold()

    if gold == None:
        # no data
        # write silver data
        #with open('gold_path', 'w') as f:
            #header 
            #f.write(f'{av_float}, 1' )# data
        headers="Time_loaded, Sum,, Count, Average".split(',')
        #current_date=datetime.datetime.now()
        #time_loaded = current_date.strftime('%Y-%M-%D %H:%M:%S')
        gold_cum=(f'{av_float}')
        print(gold_cum)
        gold_avg=(f'{av_float}')
        Column_count = 1
        #gold_data = [time_loaded, gold_cum,gold_avg,Column_count]
        gold_data = f'{time_loaded}, {gold_cum},{Column_count},{gold_avg}'.split(',')
        #file = file_opener('api_project/Storage/Gold/data_gold.csv', 'w')
        f = file_opener(gold_file, 'w')
        writer=csv.writer(f)
        writer.writerow(headers)
        writer.writerow(gold_data)
    
        # with open('api_project/Storage/Gold/data_gold.csv', 'w') as f:
        #     f.write(gold_data)
       
     
    else:      
        # with open('api_project/Storage/Gold/data_gold.csv', 'r') as file:
        #     reader = csv.reader(file)
        file = file_opener(gold_file, 'r')
        reader = csv.reader(file)
        #print (reader)
        #print ('data check')
        last_value_sum= None
        last_value_count= None
        for row in reader:
                last_value_sum = row[1]
                last_value_count=row[2]
        gold_cum=float(last_value_sum)+float(av_float)
        Column_count = int(last_value_count) + 1 
        gold_avg = gold_cum/Column_count           
        gold_data = f'{time_loaded}, {gold_cum},{Column_count},{gold_avg}'.split(',')
        # with open(gold_file, 'a', newline='') as file_append:
        #         writer=csv.writer(file_append)
        #         writer.writerow(gold_data)
        file_append= file_opener(gold_file, 'a',newline='')
        writer=csv.writer(file_append)
        writer.writerow(gold_data)        
        print(gold_data)  
            
            
            # numbers=[]
            # numbers=numbers.append(int(av_float), int(gold_cum))#gold['bpi_GBP_rate_float'])
            # gold_cum=sum(numbers)
            # gold_avg=statistics.mean(numbers)
            # gold_data = gold_data.format(gold_cum,gold_avg)     
            # with open('api_project/Storage/Gold/data_gold.csv', 'w') as f:
            #     f.write(gold_data)
            # print (gold_data)
    #return gold_data
    



    #pass


        
def gold(file_path,fileopener):
    # reading silver file

    culave(file_path,fileopener)
            
        
    #pprint(dictionary)
    
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