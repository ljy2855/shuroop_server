from dataclasses import field
from rest_framework import serializers
from .models import Profile
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        field = ('username')

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Profile
        fields = ('user_id', 'is_renting', 'left_time','user',)