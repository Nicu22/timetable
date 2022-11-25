from rest_framework import serializers
from users import models


class ProfSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Prof
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Group
        fields = '__all__'


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Room
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    room = RoomSerializer(read_only=True)
    group = GroupSerializer(read_only=True)
    prof = ProfSerializer(read_only=True)
    

    class Meta:
        model = models.Lesson
        fields = '__all__'
    
    def create(self, validated_data):
        validated_data["group_id"]=self.initial_data["group_id"]
        validated_data["room_id"]=self.initial_data["room_id"]
        validated_data["prof_id"]=self.initial_data["prof_id"]
        lesson = models.Lesson.objects.create(**validated_data)
        return lesson
    

    
"""
class LessonSerializer(serializers.ModelSerializer):
    room = RoomSerializer(read_only=True)
    group = GroupSerializer(read_only=True)
    prof = ProfSerializer(read_only=True, many=True)


    class Meta:
        model = models.Lesson
        fields = '__all__'
    
        
    def create(self, validated_data):
        validated_data["group_id"]=self.initial_data["group_id"]
        validated_data["room_id"]=self.initial_data["room_id"]
        lesson = models.Lesson.objects.create(**validated_data)
        lesson.prof.add(self.initial_data["prof"]) 
        
        return lesson
    
"""
