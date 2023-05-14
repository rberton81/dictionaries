from django.test import TestCase

from backend.models import DictWord

class DictWordTestCase(TestCase):
    def setUp(self):
        DictWord.objects.all().delete()
    
    def get_dictword(self):
        dict_word = DictWord(value="foo", origin="foo@bar.biz")
        return dict_word

    # def test_can_insert_word(self):
    #     assert DictWord.objects.count() == 0
    #     word_to_insert = self.get_dictword()
    #     word_to_insert.save()
    #     assert DictWord.objects.count() == 1
    #     word_inserted = DictWord.objects.first()
    #     assert word_inserted == word_to_insert
