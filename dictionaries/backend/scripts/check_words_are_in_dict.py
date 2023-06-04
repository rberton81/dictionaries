import argparse
from utils.utils import initialize_django

initialize_django()

from backend.clients.dictionary_clients.WordsAPIClient import WordsAPIClient
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
    
##TODO with web scrapper : https://www.oed.com/search/dictionary/?scope=Entries&q=ibm


COMPANY_PARTS = ["Inc", "Corp", "Corporation", "Ltd", "Class A", "Cls A"]
def strip_company_name(name):
    for part in COMPANY_PARTS :
        # name = name.strip(part)
        name = name.replace(part, "")
        print('it', name, part)
    return name.strip()

def main(): ##TODO add logging
    words_client = WordsAPIClient()
    parser = argparse.ArgumentParser(description="Just an example",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument("-w", "--word", help="word to look up")
    args = parser.parse_args()
    config = vars(args)

    # maybe_word = config.get("word")
    maybe_word = None
    if maybe_word:
        words_client.word_is_in_dictionary(maybe_word)
        import pdb; pdb.set_trace()
    else :
        for company in RegisteredCompany.objects.filter(integration='AlphaVantage').order_by('?'):
            print('name', company.name)
            print('stripped', strip_company_name(company.name))
            import pdb; pdb.set_trace()
            words_client.word_is_in_dictionary(company.name)

            import pdb; pdb.set_trace()


if __name__ == "__main__":
    main()
