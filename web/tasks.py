from _decimal import Decimal

from config.celery import app

from web.currency_provider.get_data import get_currencies
from web.models import Currency


@app.task(name='update_currency_dashboard')
def update_currency_dashboard():
    currencies = get_currencies()
    for code, value in currencies['data'].items():
        currency, created = Currency.objects.get_or_create(
            defaults={'value': Decimal(value['value']), 'code': code},
            code=code
        )
        if not created:
            currency.value = Decimal(value['value'])
            currency.save(update_fields=['value'])
