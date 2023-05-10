from itertools import chain

from django.core.validators import validate_email
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from django.db.models import Q
from django.shortcuts import render
import currencyapicom
import requests
from prompt_toolkit.validation import ValidationError

from .forms import ApplyForm
from .models import Currency, Apply, News

# USD = Currency.objects.filter(code="USD")
# RUB = Currency.objects.filter(code="RUB")
# EUR = Currency.objects.filter(code="EUR")
# UZS = Currency.objects.filter(code="UZS")
# all_currency = Currency.objects.exclude(Q(code="USD") | Q(code="RUB") | Q(code="EUR") | Q(code="UZS"))
# currency = list(chain(USD, EUR, RUB, UZS))
# print(currency)
# UZS = Currency.objects.filter(code="UZS").first()
# context = {"currency": currency, "UZS": UZS}


# Create your views here.


def about_company_page(request):
    RUB = Currency.objects.filter(code="RUB")
    EUR = Currency.objects.filter(code="EUR")
    UZS = Currency.objects.filter(code="UZS")
    currency = list(chain(EUR, RUB, UZS))
    UZS = Currency.objects.filter(code="UZS").first()
    context = {"currency": currency, "UZS": UZS}
    return render(request, "web/about_company.html", context)


def our_factory_page(request):
    RUB = Currency.objects.filter(code="RUB")
    EUR = Currency.objects.filter(code="EUR")
    UZS = Currency.objects.filter(code="UZS")
    currency = list(chain(EUR, RUB, UZS))
    UZS = Currency.objects.filter(code="UZS").first()
    context = {"currency": currency, "UZS": UZS}

    return render(request, "web/our_factory.html", context)


def our_products_page(request):
    RUB = Currency.objects.filter(code="RUB")
    EUR = Currency.objects.filter(code="EUR")
    UZS = Currency.objects.filter(code="UZS")
    currency = list(chain(EUR, RUB, UZS))
    UZS = Currency.objects.filter(code="UZS").first()
    context = {"currency": currency, "UZS": UZS}
    news = News.objects.all()
    context['news'] = news
    return render(request, "web/our_products.html", context)


def contact_page(request):
    RUB = Currency.objects.filter(code="RUB")
    EUR = Currency.objects.filter(code="EUR")
    UZS = Currency.objects.filter(code="UZS")
    currency = list(chain(EUR, RUB, UZS))
    UZS = Currency.objects.filter(code="UZS").first()
    context = {"currency": currency, "UZS": UZS}
    return render(request, "web/contact.html", context)


def currency_page(request):
    RUB = Currency.objects.filter(code="RUB")
    EUR = Currency.objects.filter(code="EUR")
    UZS = Currency.objects.filter(code="UZS")
    currency = list(chain(EUR, RUB, UZS))
    UZS = Currency.objects.filter(code="UZS").first()
    context = {"currency": currency, "UZS": UZS}
    return render(request, "web/currency.html", context)


def currencyapi():
    client = currencyapicom.Client('xc9TTNtkKFgqrWJy1uiZl630LyQnt80cpopjVBJE')
    data = client.latest()


class CreateApply(CreateView):
    model = Apply
    form_class = ApplyForm
    template_name = 'web/contact.html'
    success_url = '/'

    def form_valid(self, form):
        # Modelni saqlash uchun ishlatiladi
        return super().form_valid(form)




