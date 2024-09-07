from dj_rest_auth.serializers import LoginSerializer
from django.contrib.auth import authenticate
from rest_framework import serializers
from dj_rest_auth.views import LoginView


class CustomLoginSerializer(LoginSerializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        
        user = authenticate(username=username, password=password)
        if user is None:
            raise serializers.ValidationError('Unable to log in with provided credentials.')
        
        return super().validate(attrs)


class CustomLoginView(LoginView):
    serializer_class = CustomLoginSerializer