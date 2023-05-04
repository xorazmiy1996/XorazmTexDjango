from _decimal import Decimal

from config.celery import app

from web.currency_provider.get_data import get_currencies
from web.models import Currency


@app.task(name='update_currency_dashboard')
def update_currency_dashboard():
    currencies = get_currencies()
    for code, value in currencies['data'].items():
        Currency.objects.create(
            code=code,
            value=Decimal(value['value'])
        )

