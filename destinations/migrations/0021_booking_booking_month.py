# Generated by Django 4.2.16 on 2024-09-30 14:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destinations', '0020_alter_booking_package'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='booking_month',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
