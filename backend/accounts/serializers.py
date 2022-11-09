from rest_framework import serializers
from accounts import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ['username']
        #fields = '__all__'

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()