import os
import inspect

class BaseClient():
    def __init__(self, rate_limit_value=None, rate_limit_type=None):
        self.rate_limit_value = rate_limit_value
        self.rate_limit_type = rate_limit_type
        self.rate_limit_file = self.get_rate_limit_file_name()
        self.current_rate = self.get_rate_limit_from_file() or 0
        
    def get_rate_limit_file_name(self):
        class_full_path = inspect.getfile(self.__class__)
        folder_path = "/".join(class_full_path.split("/")[:-1])
        return f"{folder_path}/{self.__class__.__name__}"
        

    def get_rate_limit_from_file(self):
        if self.rate_limit_file_exists() :
            with open(self.rate_limit_file, "r") as rate_limit_file:
                rate_limit = int(rate_limit_file.read())
                print(f'found rate limit {rate_limit} in file') ##TODO use logger instead
                return rate_limit
        return None
    
    def write_rate_limit_to_file(self):
        with open(self.rate_limit_file, "w") as rate_limit_file:
            rate_limit_file.write(str(self.current_rate))
            return True
        return False
    
    def mock_call(self):
        print("I sent a mock call to an API!")
        self.current_rate += 1
        self.write_rate_limit_to_file()

    def rate_limit_file_exists(self):
        return os.path.isfile(self.rate_limit_file)

    def delete_rate_limit_file(self):
        if self.rate_limit_file_exists():
            print('try to delete file')
            os.remove(self.rate_limit_file)
