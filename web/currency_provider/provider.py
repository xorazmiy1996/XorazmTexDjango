import currencyapicom

from django.conf import settings


def get_client():
    return currencyapicom.Client(settings.CURRENCY_API_TOKEN)
