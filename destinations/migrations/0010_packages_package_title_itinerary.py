# Generated by Django 4.2.16 on 2024-09-22 18:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('destinations', '0009_remove_packages_id_packages_package_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='packages',
            name='package_title',
            field=models.CharField(default='', max_length=250, unique=True),
        ),
        migrations.CreateModel(
            name='Itinerary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_schedule', models.TextField(default='This is your Itinerary')),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itinerary', to='destinations.packages')),
            ],
        ),
    ]
