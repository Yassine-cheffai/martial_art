# Generated by Django 2.1.7 on 2021-04-14 11:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0003_competitor_weight'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competitor',
            name='weight',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(200), django.core.validators.MinValueValidator(10)]),
        ),
    ]
