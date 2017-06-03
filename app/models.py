from django.db import models

# Importing mongoengine tools and Languages, Currencies
from mongoengine import *
from django.conf.global_settings import LANGUAGES
from moneyed import CURRENCIES

class ServiceProviders(Document):
    name = StringField(max_length = 30, min_length = 3, required = True)
    email = EmailField(domain_whitelist = None, required = True)
    phone = IntField(min_length = 10, required = True)
    language = StringField(max_length = 7, choices = LANGUAGES, required = True, default = 'English')
    currency = StringField(max_length = 4, choices = CURRENCIES, required = True, default = 'USD')
    def __str__(self):
        return self.name, self.email, self.phone, self.language, self.currency

class ServiceAreas(Document):
    provider = ReferenceField(ServiceProviders)
    polygon = PolygonField(auto_index = True)
    price = IntField(min_value = 5, required = True, default = 5)

    def __str__(self):
        return self.provider, self.polygon, self.price
