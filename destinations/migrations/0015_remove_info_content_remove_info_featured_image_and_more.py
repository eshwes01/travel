# Generated by Django 4.2.16 on 2024-09-24 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destinations', '0014_packages_itinerary_delete_itinerary'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='info',
            name='content',
        ),
        migrations.RemoveField(
            model_name='info',
            name='featured_image',
        ),
        migrations.AddField(
            model_name='info',
            name='localFood',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='info',
            name='places_to_explore',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='info',
            name='things_to_do',
            field=models.TextField(default=''),
        ),
    ]
