# Generated by Django 4.2.4 on 2023-09-07 05:59

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('apis', '0002_vehicles_color'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Vehicles',
            new_name='Vehicle',
        ),
    ]