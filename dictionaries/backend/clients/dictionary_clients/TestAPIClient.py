from backend.dictionary_clients.BaseDictClient import BaseDictClient


class TestAPIClient(BaseDictClient):
    WORDS_URL = "/words/"
