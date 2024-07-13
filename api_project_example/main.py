from transformation.ingestion import ingestion
from transformation.api_silver import silver
from transformation.api_gold import gold
from pathlib import Path

root_path = Path('.')
storage_path = root_path / 'Storage'
print(storage_path)
print(root_path.cwd())
# api+project/storage


url  = 'https://api.coindesk.com/v1/bpi/currentprice.json'


def main():
    # runing ingestion
    ingestion_location = ingestion(url = url, output_location=storage_path)
    print(type(ingestion_location))
    #running silver
    silver_location = silver(storage_path, ingestion_location)
    print(silver_location)
    # running gold
    gold(storage_path, silver_location)
    # write_to_db()


if __name__ == '__main__':
    main()
