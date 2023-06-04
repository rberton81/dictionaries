

from dictionaries.backend.clients.clients.dictionary_clients.BaseDictClient import BaseDictClient


class TestAPIClient(BaseDictClient):
    WORDS_URL = "/words/"
