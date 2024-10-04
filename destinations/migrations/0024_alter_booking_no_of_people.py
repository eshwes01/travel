# Generated by Django 4.2.16 on 2024-10-04 14:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destinations', '0023_alter_booking_booking_month'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='no_of_people',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(30)]),
        ),
    ]
