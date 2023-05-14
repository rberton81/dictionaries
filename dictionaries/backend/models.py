from django.db import models

MAX_CHAR_LENGTH = 64

class DictWord(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['value', 'origin'], name='unique_word_per_origin')
        ]

    value = models.CharField(max_length=MAX_CHAR_LENGTH)
    origin = models.CharField(max_length=MAX_CHAR_LENGTH)

class Dictionary(models.Model):
    base_url = models.CharField(max_length=MAX_CHAR_LENGTH) ##TODO unique?
    name = models.CharField(max_length=MAX_CHAR_LENGTH, unique=True)
    rate_limit_value = models.IntegerField()
    rate_limit_type = models.CharField(max_length=MAX_CHAR_LENGTH) ##TODO should be choices when im figured all of them