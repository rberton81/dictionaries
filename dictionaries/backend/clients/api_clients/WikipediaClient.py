import wikipediaapi as wiki_api


class WikipediaClient :
    def __init__(self):
        self.client = wiki_api.Wikipedia('Dictionaries', 'en')

    def get_page(self, page_name):
        page_py = self.client.page(page_name)
        
        if page_py.exists():
            print("Company has a wiki page.")
            return page_py
        print("Company does not have a wiki page.")
        return None
