from rest_framework import serializers
from .models import Ride
from rootApp.models import SwiftUser


# class MessageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Message
#         exclude = ('time_sent')

class DriverUUIDSerializer(serializers.ModelSerializer):
    def create(self,validated_data):
        user = SwiftUser.objects.get(user_id=validated_data['driver'])
        return user
    
    class Meta:
        model = SwiftUser
        fields = "__all__"

class RiderUUIDSerializer(serializers.ModelSerializer):
    def create(self,validated_data):
        user = SwiftUser.objects.get(user_id=validated_data['rider'])
        return user

    class Meta:
        model = SwiftUser
        fields = "__all__"

# class RideSerializer(serializers.ModelSerializer):


#     def create(self, validated_data):

#         driver = serializers.PrimaryKeyRelatedField(read_only=True)
#         rider = serializers.PrimaryKeyRelatedField(read_only=True)
#         # collegeName = validated_data['collegeName']
#         arrival_time = validated_data['arrival_time']
#         departure_time = validated_data['departure_time']
        
#         # Retrieve the driver and rider objects
#         # driver = SwiftUser.objects.get(id=validated_data['driver'])
#         # rider = SwiftUser.objects.get(user_id=validated_data['riderUserID'])
        
#         # Retrieve the collegeName of the driver
#         print(driver)
#         collegeName = driver['collegeName']
        
#         # Assuming rider_home_location and taker_home_location need to be set based on the driver's home_location
#         rider_home_location = driver.home_location
#         taker_home_location = driver.home_location

#         # Create the Ride object with the validated data
#         ride = Ride.objects.create(
#             driver=driver,
#             rider=rider,
#             collegeName=collegeName,
#             rider_home_location=rider_home_location,
#             taker_home_location=taker_home_location,
#             arrival_time=arrival_time,
#             departure_time=departure_time
#         )   

#         return ride
    
#     class Meta:
#         model = Ride
#         fields = "__all__"
   
class RideSerializer(serializers.ModelSerializer):

    # def create(self, validated_data):
    #     # Retrieve the driver and rider objects
    #     print(validated_data)
        # driver_id = validated_data['driver']
        # rider_id = validated_data['rider']

        # Retrieve the collegeName of the driver
        # collegeName = driver.collegeName
        
        # Assuming rider_home_location and taker_home_location need to be set based on the driver's home_location
        # rider_home_location = driver.home_location
        # taker_home_location = driver.home_location

        # Extract other validated data
        # arrival_time = validated_data['arrival_time']
        # departure_time = validated_data['departure_time']

        # # Create the Ride object with the retrieved data
        # ride = Ride.objects.create(
        #     driver=driver,
        #     rider=rider,
        #     collegeName=collegeName,
        #     rider_home_location=rider_home_location,
        #     taker_home_location=taker_home_location,
        #     arrival_time=arrival_time,
        #     departure_time=departure_time
        # )   

        # return ride
    
    class Meta:
        model = Ride
        fields = "__all__"


class ShowDriverListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SwiftUser
        fields = ('username','phone','gender','profile_pic')
    