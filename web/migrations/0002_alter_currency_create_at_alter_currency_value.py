# Generated by Django 4.2 on 2023-05-04 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currency',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='currency',
            name='value',
            field=models.FloatField(),
        ),
    ]