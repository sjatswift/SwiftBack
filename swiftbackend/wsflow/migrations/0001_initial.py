# Generated by Django 4.2.4 on 2023-08-26 03:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ride',
            fields=[
                ('ride_id', models.AutoField(primary_key=True, serialize=False)),
                ('rider_home_location', models.JSONField()),
                ('taker_home_location', models.JSONField()),
                ('arrival_time', models.DateTimeField()),
                ('departure_time', models.DateTimeField()),
                ('collegename', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='driver', to=settings.AUTH_USER_MODEL)),
                ('rider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='taker', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
