from django.db import models



class Prof(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)


class Group(models.Model):
    group_name = models.CharField(max_length=10, unique=True)


class Room(models.Model):
    room_number = models.CharField(max_length=10, unique=True)


class Lesson(models.Model):

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
    prof = models.ManyToManyField(Prof)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True)
    week_day = models.IntegerField(choices=WeekDay.choices)
    lesson_type = models.IntegerField(choices=IsOdd.choices, default=IsOdd.WEEKLY)
    timeslot = models.IntegerField(choices=LessonNumber.choices)


"""
obj_name = models.ObjectName.objects.create(object_name='Ghidare',grup=grup, room=room, week_day='Luni', peer_number=1)
obj_name.prof.add(prof.instance)
"""

"""
TODO
serializers viewuri
p/u posturi?
[DONE]redenumire clase/variabile -> human readable 

"""