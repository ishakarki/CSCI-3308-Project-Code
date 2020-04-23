from django.apps import AppConfig
# in order to make the templates working, we need apps.py to add application in list
# app configuatioin
#blog config inherits app config

class BlogConfig(AppConfig):
    name = 'blog'
