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

