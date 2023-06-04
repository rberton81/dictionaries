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


    for company in RegisteredCompany.objects.filter(integration='AlphaVantage'):
        ##TODO check if in dict


    # max_count = RegisteredCompany.objects.count()
    # pks = RegisteredCompany.objects.values_list('pk', flat=True)


    # while True :
    #     no_ticker_company = get_random_company(pks)
    #     should_skip = True

    #     print(f"Trying to fetch ticker for {no_ticker_company.name}")

    #     if len(no_ticker_company.name) >= 3:
    #         import pdb; pdb.set_trace()

    #         if not should_skip :
    #             maybe_ticker = client.fetch_tickers(no_ticker_company.name)
    #             comp_data = client.fetch_company_overview(no_ticker_company.name)

    #             import pdb; pdb.set_trace()
    #             time.sleep(0.5)
    #             print('foo')


    # for no_ticker_company in RegisteredCompany.objects.filter(is_active=True,ticker__is_null=True):
        
    #     print(f"Trying to fetch ticker for {no_ticker_company.name}")
    #     should_skip=True

    #     if len(no_ticker_company.name) >= 3:
    #         import pdb; pdb.set_trace()

    #         if not should_skip :
    #             maybe_ticker = client.fetch_tickers(no_ticker_company.name)
    #             comp_data = client.fetch_company_overview(no_ticker_company.name)

    #         import pdb; pdb.set_trace()
    #         time.sleep(0.5)
    #         print('foo')


if __name__ == "__main__":
    main()
