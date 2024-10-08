# Generated by Django 4.2.16 on 2024-09-29 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('destinations', '0019_booking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='package',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='destinations.packages'),
        ),
    ]
