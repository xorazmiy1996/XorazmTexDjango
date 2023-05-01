from django.shortcuts import render


# Create your views here.

def about_company_page(request):
    return render(request, "web/about_company.html")


def our_factory_page(request):
    return render(request, "web/our_factory.html")


def our_products_page(request):
    return render(request, "web/our_products.html")


def contact_page(request):
    return render(request, "web/contact.html")
