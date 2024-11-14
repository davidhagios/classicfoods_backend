from rest_framework import serializers
from django.contrib.auth.models import User
from . models import menu


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'email', 'password']
        

class menuSerializer(serializers.ModelSerializer):
    class Meta:
        model = menu
        fields = '__all__'
