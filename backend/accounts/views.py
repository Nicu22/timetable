from rest_framework import generics
from accounts import models, serializers


class UserView(generics.ListCreateAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer