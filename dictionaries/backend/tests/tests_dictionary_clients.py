from django.test import TestCase
from backend.models import DictWord, Dictionary
from backend.clients.dictionary_clients.TestAPIClient import TestAPIClient
from backend.clients.dictionary_clients.WordsAPIClient import WordsAPIClient

class DictionaryClientTestCase(TestCase):
    fixtures = ["dictionaries.json"]
        
    def setUp(self):
        DictWord.objects.all().delete()
        Dictionary.objects.all().delete()

    def create_dictionary_client(self, name):
        Dictionary.objects.create(
            base_url = "foo.bar",
            name = name,
            rate_limit_value = 2500,
            rate_limit_type = 'rpd'
        )

    # def test_client_can_store_rate_limit(self):
    #     self.create_dictionary_client("TestAPIClient")
    #     client = TestAPIClient()
    #     client.current_rate = 0 ##TODO
    #     client.delete_rate_limit_file()
        
    #     assert client.current_rate == 0
    #     client.mock_call()
    #     assert client.current_rate == 1

    #     with open(client.rate_limit_file, "r") as rate_limit_file :
    #         current_rate = int(rate_limit_file.read())
    #         assert current_rate == 1


    def test_wordsapi_client_can_fetch(self):
        self.create_dictionary_client("WordsAPIClient")
        wordsapi_client = WordsAPIClient()

        assert DictWord.objects.count() == 0
        random_word = wordsapi_client.random()
        wordsapi_client.store_word_in_database(random_word)
        assert DictWord.objects.count() == 1
        word_db = DictWord.objects.first()
        assert word_db.value == random_word["word"]
        assert word_db.origin == "WordsAPI"

##TODO test rate limiting!!