import json
import csv
from flatten_json import flatten
import datetime
#flatten json file
#dry
def file_opener(file_location, mode):
    file = open(file_location, mode)
    return file

#read json file
def silver(storage_path, ingestion_location):

    silver_output = str(ingestion_location).replace('data', 'silver').replace('.json', '.csv').replace('Ingestion', 'Silver')

    storage_silver = storage_path / 'Silver'
    if storage_silver.exists() == False:
        storage_silver.mkdir(parents=True, exist_ok=True)

    file = file_opener(ingestion_location, 'r')
    data_trans=json.load(file)
    data_trans=flatten(data_trans)
    current_date=datetime.datetime.now()
    #adding time of tranformation
    data_trans['ETL_time'] = current_date.strftime('%Y-%M-%D %H:%M:%S')
    file.close()


    # #open a csv file for writing
    file = file_opener(silver_output, 'w')
    writer=csv.writer(file,delimiter='|')
    #write headers to csv
    headers=data_trans.keys()
    writer.writerow(headers)
    body=data_trans.values()
    writer.writerow(body)
    file.close()

    return silver_output
