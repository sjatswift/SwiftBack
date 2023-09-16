# Signals

from django.db.models.signals import post_save
from django.dispatch import receiver
from firebase_admin.messaging import Message, Notification


from .models import Ride,CurrentLocation

import channels.layers
# from    


@receiver(post_save, sender=CurrentLocation)
def locationPing(sender, instance, created, **kwargs):
    if created:
        location_data = instance.data
        instance.delete()
        print(location_data)

    Message(
    notification=Notification(title="title", body="text", image="url"),
    topic="Optional topic parameter: Whatever you want",
    )



