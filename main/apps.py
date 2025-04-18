from django.apps import AppConfig


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'


dependencies = [
    ('main', 'previous_migration_name'),
]
