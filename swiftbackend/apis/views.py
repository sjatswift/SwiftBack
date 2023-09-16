from django.shortcuts import render
from django.http import JsonResponse
import json
# Create your views here.

from rest_framework import status,exceptions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django_user_agents.utils import get_user_agent
from django.contrib.auth import login

from rest_framework_simplejwt.tokens import RefreshToken


"""
VIEW for Register API 
Method : POST
Serializer : API/Serializer/SignUpSerializer

_____________________________

INPUT (to be sent) 

password: test10_password
username: test10_name [UNIQUE]
email: test10@swift.com [UNIQUE]
gender:M [M/F]
role:Ride Taker [LIST Of OPTIONS]
collegeName:Reva University [LIST Of OPTIONS]
name:aryan thacker
profile_pic : (a file has to be sent)
license_pic : (a file has to be sent)
id_card_pic : (a file has to be sent)
phone : +919363567890 [Unique,NOT NULL]
_____________________________


"""
from .serializers import SignUpSerializer

@csrf_exempt
@api_view(['POST'])
def SignUpView(request):
    serializer = SignUpSerializer(data=request.data)
    if serializer.is_valid():
        # Hash the password before saving
        password = make_password(serializer.validated_data['password'])
        serializer.validated_data['password'] = password
        user = serializer.save()

       

        # Generate tokens for the registered user
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)

        serialized_user = LogInSerializer(user).data

        response = Response({
                'access_token': access_token,
                'user': serialized_user,
            })

        response.set_cookie(key='refreshtoken', value=refresh_token, httponly=True)

       

        return response    
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    



from .serializers import LogInSerializer
from .utils import generate_access_token,generate_refresh_token
from django.contrib import auth

"""
VIEW for Login API 
Method : POST
Serializer : API/Serializer/LogInSerializer

_____________________________

INPUT (to be sent) 

password: test10_password
username: test1LogInSerializer0_name 
_____________________________


"""

@csrf_exempt
@api_view(['POST'])
def LoginView(request):
    User = get_user_model()

    phone = request.data.get('phone')
    password = request.data.get('password')

 
    if phone is None or password is None:
        raise exceptions.AuthenticationFailed('Phone and password are rsequired')


    


    user_agent = get_user_agent(request)

    if user_agent.is_mobile:

        user = User.objects.get(phone=phone).first()

        if user is None or not user.check_password(password):
            raise exceptions.AuthenticationFailed('Invalid username or password')

        serialized_user = LogInSerializer(user).data
        # generates refrest token with user data
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)

        response = Response({
            'access_token': access_token,
            'user': serialized_user,
        })

        # sets cookie header and value (for app and website : you have to save this cookie)
        response.set_cookie(key='refreshtoken', value=refresh_token, httponly=True)

        return response

    if user_agent.is_pc:
        currentUser = User.objects.get(phone = phone)

        if currentUser.check_password(password):
            login(request,currentUser)
            context = {'message':"Auth done"}
            return JsonResponse(context)
        
        failmessage = {'message':"Auth failed"}
        return JsonResponse(failmessage)

    
"""
VIEW for Logout API 
Method : POST
"""


@csrf_exempt
@api_view(['POST'])
def LogoutView(request):

    response = Response({'message': 'Logged out successfully'})

    # Delete the refresh token cookie
    response.delete_cookie('refreshtoken')

    return response



import pyotp
import base64

@csrf_exempt
@api_view(['GET','POST'])
def OTPview(request):
    user_phone = "12191" #make this users phone number through session?
    user_phone = base64.b32encode(str(user_phone).encode())
    totp = pyotp.TOTP(user_phone,4,None,user_phone,"swiftride",120)
    
    user_agent = get_user_agent(request)


    if request.method == 'GET':
        otp = totp.now()

        return JsonResponse({"otp":otp})
    
    if request.method == 'POST':
        otp_recieved = request.data.get('otp')

        if totp.verify(otp_recieved):

            if user_agent.is_mobile: # for mobile apps
                return JsonResponse({'message':"noice"})

            if user_agent.is_pc: # for pc 
                return JsonResponse({'message':"noice"})

            if user_agent.browser.family == 'okhttp' : # for mobile web browsers
                return JsonResponse({'message':"noice"})



from .models import Vehicle
from .serializers import VehiclesSerializer 

@api_view(['GET', 'POST','PATCH'])
def VehiclesView(request):
    if request.method == 'GET':
        vehicles = Vehicle.objects.all()
        serializer = VehiclesSerializer(vehicles, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = VehiclesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PATCH':
        driver_pk = request.data.get('driver')
        vehicleToBeUpdated = Vehicle.objects.get(driver=driver_pk)
        serializer = VehiclesSerializer(vehicleToBeUpdated,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)