import requests
from backend.models import DictWord
from backend.clients.dictionary_clients.BaseDictClient import BaseDictClient

##TODO add git encrypt
class WordsAPIClient(BaseDictClient):
    WORDS_URL = "/words/"

    def __init__(self):
        super().__init__()
        self.origin = "WordsAPI"
        self.key = "foo"
        self.host = "wordsapiv1.p.mashape.com"

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
        # url = "https://wordsapiv1.p.rapidapi.com/words/"
        url = "https://wordsapiv1.p.mashape.com/words/?letters=6"
        querystring = {"random":"true"}
        headers = {
            "X-RapidAPI-Key": self.key,
            "X-RapidAPI-Host": self.host
        }
        self.write_rate_limit_to_file()
        self.current_rate += 1
        response = requests.get(url, headers=headers, params=querystring)
        ##TODO check status, if ok 
        if response.status_code == 200 :
            resp = response.json()
            return resp
        
        print('got error')
        import pdb; pdb.set_trace()
        print('foo')


    ##TODO store the associated word, add FK on company
    def word_is_in_dictionary(self, word):
        url = "https://wordsapiv1.p.mashape.com/words/{word}/definitions"
        headers = {
            "X-RapidAPI-Key": self.key,
            "X-RapidAPI-Host": self.host
        }
        self.write_rate_limit_to_file()
        self.current_rate += 1
        response = requests.get(url, headers=headers)
        ##TODO check status, if ok 
        if response.status_code == 200 :
            resp = response.json()
            import pdb; pdb.set_trace()
            return resp
        
        print('got error')
        import pdb; pdb.set_trace()
        print('foo')