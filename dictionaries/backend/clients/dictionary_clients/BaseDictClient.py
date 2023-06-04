from backend.models import Dictionary
from backend.clients.BaseClient import BaseClient

class BaseDictClient(BaseClient):
    def __init__(self):
        super().__init__()

        try :
            db_row = Dictionary.objects.get(name=self.__class__.__name__)
        except Dictionary.DoesNotExist :
            print(f'dictionary not found in database : {self.__class__.__name__}')
            raise
             
        self.base_url = db_row.base_url
        self.name = db_row.name
        self.rate_limit_value = db_row.rate_limit_value
        self.rate_limit_type = db_row.rate_limit_type
        