"""Module default confing django apps"""
from django.apps import AppConfig


class TestappConfig(AppConfig):
    """Class default confing django app: testapp"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'testapp'
