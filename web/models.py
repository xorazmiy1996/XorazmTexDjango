from django.db import models


# Create your models here.

class Currency(models.Model):
    code = models.CharField(max_length=3)
    value = models.FloatField()
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.code
