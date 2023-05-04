from django.db import models


# Create your models here.

class Currency(models.Model):
    country_code = models.CharField(max_length=3)
    value = models.DecimalField(max_digits=6, decimal_places=3)

    def __str__(self):
        return self.country_code
