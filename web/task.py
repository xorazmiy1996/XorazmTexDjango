from config.celery import app

from web.currency_provider.get_data import get_currencies


@app.task(name='update_currency_dashboard')
def update_currency_dashboard():
    currencies = get_currencies()
