import requests

from backend.dictionary_clients.BaseDictClient import BaseDictClient
from backend.models import DictWord


class WordsAPIClient(BaseDictClient):
    WORDS_URL = "/words/"

    def __init__(self):
        super().__init__()
        self.origin = "WordsAPI"

    def store_word_in_database(self, word_json):
        word_value = word_json["word"]
        try :
            DictWord.objects.create(
                value = word_value,
                origin = self.origin, 
            )
            return True
        
        except Exception as error :
            print('got error')
            import pdb; pdb.set_trace() ##TODO
        return False
    
    ##TODO must check rate limit before ANY request
    def random(self):
        url = "https://wordsapiv1.p.rapidapi.com/words/"
        querystring = {"random":"true"}
        headers = {
            "X-RapidAPI-Key": "ec6a953992mshf82db23974f9d9ep123ecejsn0b6d0e97817b",
            "X-RapidAPI-Host": "wordsapiv1.p.rapidapi.com"
        }
        response = requests.get(url, headers=headers, params=querystring)
        self.current_rate += 1
        self.write_rate_limit_to_file()
        ##TODO check status, if ok 
        if response.status_code == 200 :
            return response.json()
        
        print('got error')
        import pdb; pdb.set_trace()
        print('foo')