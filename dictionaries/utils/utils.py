import os

def initialize_django(settings_module="dictionaries.settings"):
    os.environ["DJANGO_SETTINGS_MODULE"] = settings_module
    import django

    django.setup()
