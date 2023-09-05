from rest_framework import authentication
from rest_framework import exceptions
from django.contrib.auth import authenticate, get_user_model
from rootApp.models import SwiftUser

class MainAuthBackend(authentication.BaseAuthentication):
    def authenticate(self, request):
        phone = request.data.get('phone')
        password = request.data.get('password')


        if not phone or not password:
            raise exceptions.AuthenticationFailed('No credentials provided.')

        credentials = {
            get_user_model().USERNAME_FIELD: password,
            'password': password
        }

        user = authenticate(**credentials)

        if user is None:
            raise exceptions.AuthenticationFailed("User doesn't exists")
        

        return (user,None)