import json
import csv
from flatten_json import flatten
import datetime
from collections import defaultdict
from pprint import pprint
from pathlib import Path


dictionary= defaultdict(list)



def read_silver(file_path):
    global dictionary
    with open(file_path,'r') as f:

            header = None
            csv_reader= f.readlines()
            for indx, i in enumerate(csv_reader):

                item = i.split('|')
                item = [ x.strip() for x in item]

                if indx == 0: # the header will always be 0
                    header = item
                else:
                    body = item
                    if header is None:
                        raise Exception('Error!! Data is corrupt')


                    for key, value in zip(header, body):
                         dictionary[key].append(value)
                # item = dict(zip(header,body))

    return dictionary

def get_gold(gold_path):

    if gold_path.exists() == False:
        return None

    with open(gold_path, 'r') as f:
        data = f.read()
        return data

def get_gold_path(file_path):
    file_path = file_path / 'Gold'
    global GOLD_PATH
    GOLD_PATH = file_path / 'data_gold.txt'
    if file_path.exists() == False:
        file_path.mkdir(parents=True, exist_ok=True)


def culave(silver_file_path):
     # value from silver

    time_format = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    silver = read_silver(silver_file_path)
    gbp_av_float = silver['bpi_GBP_rate_float'].pop()
    eur_av_float = silver['bpi_EUR_rate_float'].pop()
    usd_av_float = silver['bpi_USD_rate_float'].pop()
     #value from gold
    print(eur_av_float, gbp_av_float, usd_av_float)

    initial_count = 1


    gold= get_gold(GOLD_PATH)
    if gold == None:
          # no data
        # write silver data
        with open(GOLD_PATH, 'w') as f:
            #header
            f.write(f'time_updated|av_gbp_rate|av_usd_rate|av_eur_rate|total_count|total_sum_gbp|total_sum_usd|total_sum_eur \n' )
            f.write(f'{time_format}|{gbp_av_float}|{eur_av_float}|{usd_av_float}|{initial_count}|{gbp_av_float}|{eur_av_float}|{usd_av_float} \n' )# data
    else:
        # data exists
        gold = gold.split('\n')
        header = gold.pop(0)
        body = gold.pop(0)
        body = body.split('|')
        total_count = int(body[4]) + 1
        total_sum_gbp = float(body[5]) + float(gbp_av_float)
        total_sum_usd = float(body[6]) + float(usd_av_float)
        total_sum_eur = float(body[7]) + float(eur_av_float)
        gbp_av_float = (total_sum_gbp + float(gbp_av_float))/total_count
        usd_av_float = (total_sum_usd + float(usd_av_float)) / total_count
        eur_av_float = (total_sum_eur + float(eur_av_float)) / total_count
        # write silver data
        with open(GOLD_PATH, 'a') as f:
            #header
            f.write(f'{time_format}|{gbp_av_float}|{eur_av_float}|{usd_av_float}|{total_count}|{total_sum_gbp}|{total_sum_usd}|{total_sum_eur} \n' )





def gold(storage_path, silver_file_path):
    # reading silver file
    #create gold directory
    get_gold_path(storage_path)


    culave(silver_file_path)


    pprint(dictionary)
    # write your gold logic here
