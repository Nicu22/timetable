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
    room_id = RoomSerializer(read_only=True, many=True)
    group_id = GroupSerializer(read_only=True, many=True)
    prof = ProfSerializer(read_only=True)
    

    class Meta:
        model = models.Lesson
        fields = '__all__'
    
    def create(self, validated_data):
        validated_data["group_id"]=self.initial_data["group"]
        validated_data["room_id"]=self.initial_data["room"]
        breakpoint()
        lesson = models.Lesson.objects.create(**validated_data)
        lesson.prof.add(self.initial_data["prof"]) 
        
        return lesson
    #Fix The Error serializer.data

