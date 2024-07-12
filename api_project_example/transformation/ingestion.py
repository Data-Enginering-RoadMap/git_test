import os
import requests
import json
from datetime import datetime
import csv
from pathlib import Path
from typing import List, Union
url  = 'https://api.coindesk.com/v1/bpi/currentprice.json'


def ingestion(url:str, output_location: Path)-> Union[Path, None]:
    try:
        time_format = datetime.now().strftime("%Y%m%d%H%M%S")
        response = requests.get(url)
        # the move the api to a json file
        data = response.json()
        directory = output_location /'Ingestion'
        path = directory / f'data_{time_format}.json'
        # check if files exists else create
        if directory.exists() == False:
            directory.mkdir(parents=True, exist_ok=True)
        with open(str(path) , 'w') as json_file:
            json.dump(data, json_file,indent =4)
        return path
    except Exception as e:
        print(e)
