from django.apps import AppConfig


class SoftDeskConfig(AppConfig):
    """Configure app settings."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'softdesk'
    verbose_name = "SoftDesk"
