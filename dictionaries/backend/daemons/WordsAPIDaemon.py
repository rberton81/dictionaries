from utils.utils import initialize_django

initialize_django()

from backend.models import DictWord
from backend.clients.dictionary_clients.WordsAPIClient import WordsAPIClient


def is_new_word(word, origin):
    return not DictWord.objects.filter(
        value = word,
        origin = origin
    ).exists()

def main(): ##TODO add logging
    client = WordsAPIClient()
    while client.current_rate < client.rate_limit_value :
        maybe_new_word = client.random()["word"]
        # print(f"word {maybe_new_word} fetched from {client.origin}")
        if is_new_word(maybe_new_word, client.origin) :
            DictWord.objects.create(
                value=maybe_new_word,
                origin=client.origin
            )
            # print('created a new word in the database!')
        else :
            print(f"word was already in the database")
        sleep_time = 0.025
        # print(f'gonna sleep {sleep_time} seconds now!')
        import time; time.sleep(sleep_time)
    print('exceeded rate limit!')
    return


if __name__ == "__main__":
    main()
