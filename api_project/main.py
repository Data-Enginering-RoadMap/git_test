from transformation.ingestion import ingestion 
from transformation.api_silver import silver
from pathlib import Path

root_path = Path('.')
storage_path = root_path / 'api_project/Storage'
print(storage_path)
# api+project/storage


url  = 'https://api.coindesk.com/v1/bpi/currentprice.json'


def main():
    ingestion_location = ingestion(url = url, output_location=storage_path)
    print(ingestion_location)
    silver_location = silver(ingestion_location)
    print(silver_location)
    # gold()
    # write_to_db()


if __name__ == '__main__':
    print('hello world')
    main()