from rest_framework import generics, decorators, response, status
from accounts import models, serializers


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
    data = {
        'email': serializer.data['email'],
        'password': serializer.data['password'],
        'token': user.auth_token.key
    }
    return response.Response(data)
    

#TODO: la logare – token