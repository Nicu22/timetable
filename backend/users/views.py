from rest_framework import generics
from users import models, serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class LessonView(generics.ListCreateAPIView):
    queryset = models.Lesson.objects.all()
    serializer_class = serializers.LessonSerializer

    
class LessonDetailedView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Lesson.objects.all()
    serializer_class = serializers.LessonSerializer


class ProfView(generics.ListCreateAPIView):
    queryset = models.Prof.objects.all()
    serializer_class = serializers.ProfSerializer 


class ProfDetailedView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Prof.objects.all()
    serializer_class = serializers.ProfSerializer 

    
class GroupView(generics.ListCreateAPIView):
    queryset = models.Group.objects.all()
    serializer_class = serializers.GroupSerializer 


class GroupDetailedView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Group.objects.all()
    serializer_class = serializers.GroupSerializer 
    
    
class RoomView(generics.ListCreateAPIView):
    #permission_classes = [IsAuthenticated]
    queryset = models.Room.objects.all()
    serializer_class = serializers.RoomSerializer 
   
    
class RoomDetailedView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Room.objects.all()
    serializer_class = serializers.RoomSerializer 
