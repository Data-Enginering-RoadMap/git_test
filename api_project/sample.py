
ingestion_location = 'api_project/Storage/Ingestion/data_20240615.json'
silver_output = ingestion_location.replace('data', 'silver').replace('.json', '.csv')


print(silver_output, 'after')
