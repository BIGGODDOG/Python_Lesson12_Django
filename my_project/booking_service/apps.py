from django.apps import AppConfig


class BookingServiceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'booking_service'

    def ready(self) -> None:
        import booking_service.signal