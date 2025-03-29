from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.authtoken.models import Token

User = get_user_model()

class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField()
    class Meta:
        model = get_user_model()
        fields = ('username', 'password', 'email', 'bio', 'profile_picture')
    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'bio', 'profile_picture', 'followers')