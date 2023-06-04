import os
import requests
import csv

from backend.clients.clients.BaseClient import BaseClient
from backend.models import RegisteredCompany

class AlphaVantageClient(BaseClient):
    def __init__(self):
        super().__init__(rate_limit_value=5, rate_limit_type="rpm")
        self.api_key = os.getenv("OPENAI_API_KEY")

    def fetch_tickers(self, keyword):
        url = f"https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={keyword}&apikey={self.api_key}"

        print(f"Will fetch company tickers for {keyword}")

        response = requests.get(url)
        data = response.json()

        print('response', response)
        print('data', data)

        return data

    def fetch_company_overview(self, keyword):
        url = f"https://www.alphavantage.co/query?function=OVERVIEW&symbol={keyword}&apikey={self.api_key}"

        print(f"Will fetch company details for {keyword}")

        response = requests.get(url)
        data = response.json()

        print('response', response)
        print('data', data)

        return data

    def fetch_all_listed_us_companies(self, state="active"):
        url = f"https://www.alphavantage.co/query?function=LISTING_STATUS&apikey={self.api_key}&state={state}"

        with requests.Session() as session:
            download = session.get(url
                                   )
            decoded_content = download.content.decode('utf-8')
            cr = csv.reader(decoded_content.splitlines(), delimiter=',')
            rows = list(cr)
            count = 0
            for row in rows:
                count += 1
                if count == 1:
                    continue
                ticker, name, exchange, asset_type, ipo_date, delist_date, status = row
                import pdb; pdb.set_trace()
                company = RegisteredCompany.objects.create(
                    asset_type=asset_type,
                    exchange=exchange,
                    name=name,
                    integration='AlphaVantage',
                    is_active = True if status == 'active' else False,
                    ipo_date = ipo_date,
                    status=status,
                    ticker=ticker

                )