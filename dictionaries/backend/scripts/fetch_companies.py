from utils.utils import initialize_django

initialize_django()

from backend.clients.clients.api_clients.AlphaVantageClient import AlphaVantageClient
from backend.models import RegisteredCompany

import time
import random

def get_random_company(pks):
    random_pk = random.choice(pks)
    try :
        no_ticker_company = RegisteredCompany.objects.get(pk=random_pk)
    except RegisteredCompany.DoesNotExist :
        return get_random_company(pks)
    return no_ticker_company
    

def main(): ##TODO add logging
    client = AlphaVantageClient()
    client.fetch_all_listed_us_companies()
    

if __name__ == "__main__":
    main()
