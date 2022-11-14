from rest_framework import generics, decorators, response, status
from accounts import models, serializers
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
#for time check on token authentication:
import datetime
import pytz
from django.utils import timezone
from django.conf import settings
from accounts import models


class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })

class UserView(generics.ListCreateAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer

@decorators.api_view(['POST'])
def login_view(request):
    serializer = serializers.LoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    try:
        user = models.User.objects.get(email=serializer.data['email'])
    except models.User.DoesNotExist:
        msg = {'error': 'USER DOES NOT EXIST'}
        return response.Response(msg, status=status.HTTP_404_NOT_FOUND)
    if user.check_password(serializer.data['password']) is False:
        msg = {'error': 'WRONG PASSWORD'}
        return response.Response(msg, status=status.HTTP_400_BAD_REQUEST)
    
    #date202211111452
    user.auth_token.key = Token.generate_key()  
    
    data = {
        #'email': serializer.data['email'],
        #'password': serializer.data['password'],
        'token': user.auth_token.key
    }
    
    return response.Response(data)
    
#TODO: la logare – token



'''@decorators.api_view(['POST'])
def login_try(request):
    sesrializer = serializers.LoginSerializer(data=request.data)
'''