from django.db import models
from rootApp.models import SwiftUser
import uuid

# Create your models here.
class Ride(models.Model):
    ride_id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    
    # exisiting information
    driver = models.ForeignKey(SwiftUser, related_name = 'driver' ,on_delete=models.CASCADE)
    rider = models.ForeignKey(SwiftUser, related_name='taker' ,on_delete=models.CASCADE)

    # common existing information , selected in booking flow ?
    collegeName = models.TextField(max_length=200)

    # Location of rider and taker
    rider_home_location = models.JSONField()  
    taker_home_location = models.JSONField()

    # ask user to input
    arrival_time = models.DateTimeField()
    departure_time = models.DateTimeField()

    status_CHOICES = [
        ('Arrived', 'Arrived'),
        ('En Route', 'En Route'),
        ('Waiting for Pickup', 'Waiting for Pickup'),
        ('In Progress - En Route', 'In Progress - En Route'),
        ('In Progress - On Pickup', 'In Progress - On Pickup'),
        ('Cancelled', 'Cancelled'),
        ('Booked', 'Booked'),
        ('Completed', 'Completed'),
        ('Delayed', 'Delayed'),
        ('Driver Assigned', 'Driver Assigned'),
        ('Payment Pending', 'Payment Pending'),
        ('Review Pending', 'Review Pending'),
        ('Expired', 'Expired'),
        ('Rescheduled', 'Rescheduled'),
        ('No Show', 'No Show'),
    ]
    
    current_status = models.CharField(max_length=30, choices=status_CHOICES, default='Booked')


class CurrentLocation(models.Model):
    ride = models.OneToOneField(Ride,on_delete=models.CASCADE)
    current_location = models.JSONField(default=None)
 