
import requests
import json
from datetime import datetime
import csv
from api_project.utility.utils import time_exec
url  = 'https://api.coindesk.com/v1/bpi/currentprice.json'

def time_exec(func_name):
    execution_time=datetime.now().strftime('%Y-%M-%D %H:%M:%S')
    print(f'Execution time for {func_name}:{execution_time}')


def ingestion(url, output_location):
    try: 
        time_format = datetime.now().strftime("%Y%m%d%H%M%S")
        response = requests.get(url)
        # the move the api to a json file
        data = response.json()
        path = f'{output_location}/Ingestion/data_{time_format}.json'
        with open(path , 'w') as json_file:
            json.dump(data, json_file,indent =4)
    except Exception as e:
        print(e)
    time_exec('Ingestion')
    return path