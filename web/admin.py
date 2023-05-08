from django.contrib import admin

# Register your models here.
from .models import Currency,Apply,News
from parler.admin import TranslatableAdmin

admin.site.register(Currency)
admin.site.register(Apply,TranslatableAdmin)
admin.site.register(News,TranslatableAdmin)
