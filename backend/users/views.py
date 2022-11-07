from rest_framework import generics
from users import models, serializers


class LessonView(generics.ListCreateAPIView):
    queryset = models.Lesson.objects.all()
    serializer_class = serializers.LessonSerializer


class ProfView(generics.ListCreateAPIView):
    queryset = models.Prof.objects.all()
    serializer_class = serializers.ProfSerializer 


class GroupView(generics.ListCreateAPIView):
    queryset = models.Group.objects.all()
    serializer_class = serializers.GroupSerializer 


class RoomView(generics.ListCreateAPIView):
    queryset = models.Room.objects.all()
    serializer_class = serializers.RoomSerializer 
