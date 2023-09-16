# Generated by Django 4.2.4 on 2023-09-10 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wsflow', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RideState',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_status', models.CharField(choices=[('Arrived', 'Arrived'), ('En Route', 'En Route'), ('Waiting for Pickup', 'Waiting for Pickup'), ('In Progress - En Route', 'In Progress - En Route'), ('In Progress - On Pickup', 'In Progress - On Pickup'), ('Cancelled', 'Cancelled'), ('Booked', 'Booked'), ('Completed', 'Completed'), ('Delayed', 'Delayed'), ('Driver Assigned', 'Driver Assigned'), ('Payment Pending', 'Payment Pending'), ('Review Pending', 'Review Pending'), ('Expired', 'Expired'), ('Rescheduled', 'Rescheduled'), ('No Show', 'No Show')], default='Booked', max_length=30)),
                ('Ride', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='wsflow.ride')),
            ],
        ),
    ]