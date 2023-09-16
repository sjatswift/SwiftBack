from typing import Type
from django.db.models import QuerySet
from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
from   djangochannelsrestframework.decorators import action
from djangochannelsrestframework.mixins import CreateModelMixin,PaginatedModelListMixin
from rest_framework.serializers import Serializer
from rest_framework.response import Response
from rest_framework import status

from .serializers import RideSerializer,ShowDriverListSerializer
from apis.serializers import SignUpSerializer
from .models import Ride,CurrentLocation
from rootApp.models import SwiftUser
import json
from asgiref.sync import async_to_sync,sync_to_async
from .signals import change_of_state_signal 

# permissions
from rest_framework.permissions import IsAuthenticated
from rootApp.permissions import IsTaker

class flowConsumer(CreateModelMixin,PaginatedModelListMixin, GenericAsyncAPIConsumer):
    queryset = Ride.objects.all()
    serializer_class = RideSerializer

    def get_queryset(self, **kwargs) -> QuerySet:
    

        if kwargs['action'] == 'list':
            collegeName = kwargs['collegeName']
            return SwiftUser.objects.filter(collegeName=collegeName)
        return super().get_queryset(**kwargs)

 
    def get_serializer_class(self, **kwargs) -> type[Serializer]:
        if kwargs['action'] == 'list':
            return ShowDriverListSerializer
        
        return super().get_serializer_class(**kwargs)

  

    @action() 
    async def  handle_location_update(self, **kwargs):
        latitude = kwargs.get('latitude')
        longitude = kwargs.get('longitude')

        location_json =   {
            'type': 'location_update',
            'latitude': latitude,
            'longitude': longitude,
        }

        await self.send(json.dumps({
            "type":"websocket.send",
            "location": location_json
        }))

        current_location_json = {
            'latitude': latitude,
            'longitude': longitude,
        }

        current_ride = await sync_to_async(Ride.objects.get)(ride_id = "5ea2219a-efe4-4851-8335-f0cce663b389") 
        current_location = CurrentLocation(ride = current_ride , current_location = current_location_json )

        await sync_to_async(current_location.save)(location_json)

        # return location_json, 200

    @action()       
    def list(self, **kwargs):
        if kwargs['collegeName'] == "":
            # return async_to_sync(self.handle_exception)(KeyError, "list", kwargs["request_id"])
            return "Please enter a college name", 400
        data, response = async_to_sync(super().list)(**kwargs)
        return data, response
 
    @action()
    def start_ride(self, **kwargs):
        change_of_state_signal.send(sender=SwiftUser,state_option="En Route")
        return "started" , 200