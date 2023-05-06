from django.urls import path,include
from .views import about_company_page,our_factory_page,our_products_page,contact_page,currency_page
# app_name='lang'


urlpatterns = [
    path('', about_company_page, name='about_company_page_url'),
    path('our_factory/', our_factory_page, name='our_factory_page_url'),
    path('our_product/', our_products_page, name='our_products_page_url'),
    path('contact/', contact_page, name='contact_page_url'),
    path('currency/', currency_page, name='currency_page_url'),
]
