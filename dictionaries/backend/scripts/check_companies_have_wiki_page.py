import argparse
from backend.clients.api_clients.WikipediaClient import WikipediaClient
from utils.utils import initialize_django
import requests
import datetime

initialize_django()

from backend.models import RegisteredCompany

COMPANY_PARTS = [
    "Inc.", 
    "Inc", 
    "Corp.", 
    "Corp" , 
    "Corporation", 
    "Ltd.", 
    "Ltd", 
    "Class A", 
    "Cls A", 
    "S.A.", #FIX
    # "Holdings", #FIX
    # "Holding", #FIX
    "plc", #FIX
    ]

def strip_company_name(name):
    for part in COMPANY_PARTS :
        # name = name.strip(part)
        name = name.replace(part, "")
        # print('it', name, part)
    return name.strip()

def to_wiki_page_name(company_name):
    stripped_name = strip_company_name(company_name)
    page_name = "_".join(stripped_name.split(" "))
    print(f"Looking for page named {page_name}")
    return page_name

def get_page_views(page_name): ##TODO date is start / end
    project = "en.wikipedia"
    access = "all-access"
    agent = "all-agents"
    # granularity = "monthly"
    today=datetime.datetime.today()
    last_month = today - datetime.timedelta(days=31)
    today_formatted = today.strftime("%Y%m%d")
    last_month_formatted = last_month.strftime("%Y%m%d")

    # granularity = "yearly"
    # start_year = "2022"  # Start year
    # end_year = "2023"    # End year

    granularity = "monthly"
    start_date = "20230101"
    end_date = "20230131"

    headers = {'User-Agent': 'BobsBot/0.0 (https://example.org/idonthaveapagesorry/; test@test.test)'}
    # url = f"https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/{project}/{access}/{agent}/{page_name}/{granularity}/{last_month_formatted}/{today_formatted}"
    # url = f"https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/{project}/{access}/{agent}/{page_name}/{granularity}/{start_year}/{end_year}"
    url = f"https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/{project}/{access}/{agent}/{page_name}/{granularity}/{start_date}/{end_date}"
    print('Trying to get view count')
    response = requests.get(url, headers=headers)
    
    try:
        data = response.json()
        view_count = data["items"][0]["views"]
        print(f"Page has {view_count} views.") 
        return view_count
    except Exception as error:
        print(f"Got error {error}")
        return None
    

##TODO we can try other languages on Wikipedia too !
def main(): ##TODO add logging
    wiki_client = WikipediaClient()
    parser = argparse.ArgumentParser(description="Just an example",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument("-w", "--word", help="word to look up")
    args = parser.parse_args()
    config = vars(args)

    # for company in RegisteredCompany.objects.filter(integration="IPO").exclude(wiki_page=""):
    for company in RegisteredCompany.objects.filter(integration="IPO"):
        print(f"Checking if company {company.name} has a wiki page...")
        page_name = to_wiki_page_name(company.name)
        maybe_wiki_page = wiki_client.get_page(page_name)
        if maybe_wiki_page:
            view_count = get_page_views(page_name)
            company.wiki_page = maybe_wiki_page.fullurl
            company.wiki_page_views = view_count
        else:
            company.wiki_page=""
        company.save()
        

if __name__ == "__main__":
    main()
