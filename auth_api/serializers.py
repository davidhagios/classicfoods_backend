from rest_framework import serializers
from django.contrib.auth.models import User
from . models import Task, Profile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'email', 'password']
        

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        

class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['picture']