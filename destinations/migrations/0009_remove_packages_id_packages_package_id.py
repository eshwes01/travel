# Generated by Django 4.2.16 on 2024-09-22 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destinations', '0008_alter_packages_destination'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='packages',
            name='id',
        ),
        migrations.AddField(
            model_name='packages',
            name='package_id',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
    ]