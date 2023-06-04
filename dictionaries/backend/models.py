from django.db import models

MAX_CHAR_LENGTH = 64
MAX_LONG_CHAR_LENGTH = 256

class DictWord(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['value', 'origin'], name='unique_word_per_origin')
        ]

    value = models.CharField(max_length=MAX_CHAR_LENGTH)
    origin = models.CharField(max_length=MAX_CHAR_LENGTH)

class Dictionary(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['base_url', 'name'], name='unique__dict__api')
        ]

    base_url = models.CharField(max_length=MAX_CHAR_LENGTH)
    name = models.CharField(max_length=MAX_CHAR_LENGTH)
    rate_limit_value = models.IntegerField()
    rate_limit_type = models.CharField(max_length=MAX_CHAR_LENGTH) ##TODO should be choices when im figured all of them

class RegisteredCompany(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name', 'ticker'], name='name__ticker__unique_together')
        ]

    asset_type = models.CharField(max_length=MAX_LONG_CHAR_LENGTH, null=True, default=None)
    exchange = models.CharField(max_length=MAX_LONG_CHAR_LENGTH, null=True, default=None)
    # has_wiki_page = models.BooleanField(default=False)
    name = models.CharField(max_length=MAX_LONG_CHAR_LENGTH)
    industry = models.CharField(max_length=MAX_LONG_CHAR_LENGTH, null=True, default=None)
    integration = models.CharField(max_length=MAX_LONG_CHAR_LENGTH, default=None)
    is_active = models.BooleanField(default=True)
    is_in_dictionary = models.BooleanField(default=False)
    ipo_date = models.CharField(max_length=MAX_LONG_CHAR_LENGTH, null=True, default=None) ##TODO should be datetimefield
    status = models.CharField(max_length=MAX_CHAR_LENGTH, null=True, default="active")
    ticker = models.CharField(max_length=MAX_CHAR_LENGTH, default=None, null=True)
    wiki_page = models.CharField(max_length=MAX_LONG_CHAR_LENGTH, default=None)
    wiki_page_views = models.IntegerField(null=True, default=None)
    