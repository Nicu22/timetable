from django.db import models
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView



class Prof(models.Model):
    first_name = models.CharField(max_length=50, unique=True)
    last_name = models.CharField(max_length=50, unique=True)


class Group(models.Model):
    group_name = models.CharField(max_length=10, unique=True)


class Room(models.Model):
    room_number = models.CharField(max_length=10, unique=True)


class Lesson(models.Model, APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    
    class IsOdd(models.IntegerChoices):
        WEEKLY = 0    
        ODD = 1
        EVEN = 2


    class LessonNumber(models.IntegerChoices):
        ONE = 1
        TWO = 2
        THREE = 3
        FOUR = 4
        FIVE = 5
        SIX = 6
        SEVEN = 7


    class WeekDay(models.IntegerChoices):
        MONDAY = 1
        TUESDAY = 2
        WEDNESDAY = 3
        THURSDAY = 4
        FRIDAY = 5
        SATURDAY = 6 


    lesson_name = models.CharField(max_length=50)
    prof = models.ForeignKey(Prof, on_delete=models.CASCADE, null=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True)
    week_day = models.IntegerField(choices=WeekDay.choices)
    lesson_type = models.IntegerField(choices=IsOdd.choices, default=IsOdd.WEEKLY)
    timeslot = models.IntegerField(choices=LessonNumber.choices)

