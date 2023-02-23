from rest_framework import serializers
from django.contrib.auth.models import User

from .models import UserProfile


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta: 
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'password']

class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = '__all__'