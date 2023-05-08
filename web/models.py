from django.db import models
from parler.models import TranslatableModel, TranslatedFields


# Create your models here.

class Currency(models.Model):
    code = models.CharField(max_length=3)
    value = models.FloatField()
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.code


class Apply(TranslatableModel):
    translations = TranslatedFields(
        full_name=models.CharField(max_length=50),
        email=models.CharField(max_length=30),
        text=models.TextField(max_length=1000),
    )

    def __str__(self):
        return self.email


class News(TranslatableModel):
    translations = TranslatedFields(
        topic=models.CharField(max_length=80),
        image=models.ImageField(upload_to='image/'),
        description=models.TextField(max_length=1000),
        create_at=models.DateTimeField(auto_now_add=True)
    )

    def __str__(self):
        return self.topic
