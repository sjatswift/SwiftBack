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
from .models import Ride
from rootApp.models import SwiftUser
import json
from asgiref.sync import async_to_sync


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

    # def filter_queryset(self, queryset: QuerySet, **kwargs) -> QuerySet:
    #     return super().filter_queryset(queryset, **kwargs)

    def get_serializer_class(self, **kwargs) -> type[Serializer]:
        if kwargs['action'] == 'list':
            return ShowDriverListSerializer
        
        return super().get_serializer_class(**kwargs)

    # async def websocket_receive(self, event):
    #     text_data = event.get("text")
    #     json_data = json.loads(text_data)

    #     message_type = json_data.get('type')
    #     if message_type == 'location_update':
    #          self.handle_location_update(json_data)
    #     elif message_type == 'show_drivers':
    #          self.handle_show_drivers(json_data)

    @action() 
    def handle_location_update(self, **kwargs):

        latitude = kwargs.get('latitude')
        longitude = kwargs.get('longitude')

        location_json =   {
            'type': 'location_update',
            'latitude': latitude,
            'longitude': longitude,
        }

        return location_json, 200

    @action()       
    def list(self, **kwargs):
        if kwargs['collegeName'] == "":
            # return async_to_sync(self.handle_exception)(KeyError, "list", kwargs["request_id"])
            return "Please enter a college name", 400
        data, response = async_to_sync(super().list)(**kwargs)
        return data, response
 
        # print(json.dumps(location_json))
        # self.send_json(json.dumps(location_json))

    # def handle_message_update(self, data):
    #     ride_id = data.get('ride_id')
    #     message_text = data.get('message_text')
    #     sender_id = data.get('sender_id')
    #     receiver_id = data.get('receiver_id')

    #     try:
    #         room = Ride.objects.get(id=ride_id)
    #         sender = SwiftUser.objects.get(id=sender_id)
    #         receiver = SwiftUser.objects.get(id=receiver_id)

    #         message = Message.objects.create(
    #             room=room,
    #             message_text=message_text,
    #             sender=sender,
    #             receiver=receiver
    #         )

    #         # Broadcast the message to all users in the same room
    #         self.send_group_message({
    #             'type': 'message_update',
    #             'message': {
    #                 'id': message.id,
    #                 'room_id': str(room.id),
    #                 'message_text': message_text,
    #                 'sender_id': str(sender.id),
    #                 'receiver_id': str(receiver.id),
    #                 'time_sent': message.time_sent.isoformat(),
    #             }
    #         })

    #     except (Ride.DoesNotExist, SwiftUser.DoesNotExist):
    #         pass


    # @action() 
    # def handle_show_drivers(self, **kwargs):
    #     # permission_classes = [IsTaker]
    #     collegeName = kwargs.get('collegeName')
    #     users = self.handle_user_queryset(collegeName)
    #     user_data = SignUpSerializer(users,many=True).data
    #     driverlist_json = {
    #         'type': 'show_drivers',
    #         'driverlist': user_data,
    #     }

    #     self.send(json.dumps(driverlist_json))

