# Generated by Django 4.2.16 on 2024-09-20 13:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('destinations', '0004_packages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='packages',
            name='destination',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='destination', to='destinations.destination'),
        ),
    ]
