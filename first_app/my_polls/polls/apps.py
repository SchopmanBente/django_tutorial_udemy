from django.apps import AppConfig
from django.utils.autoreload import autoreload_started


class PollsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'polls'

