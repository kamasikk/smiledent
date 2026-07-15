from django.conf import settings


def clinic_settings(request):
    """Робить контактні дані клініки доступними у всіх шаблонах."""
    return {
        'SITE_NAME': settings.SITE_NAME,
        'SITE_URL': settings.SITE_URL,
        'CLINIC_PHONE': settings.CLINIC_PHONE,
        'CLINIC_EMAIL': settings.CLINIC_EMAIL,
        'CLINIC_ADDRESS': settings.CLINIC_ADDRESS,
        'CLINIC_LAT': settings.CLINIC_LAT,
        'CLINIC_LNG': settings.CLINIC_LNG,
    }
