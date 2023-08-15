from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class RegisterSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    email = serializers.CharField()
    password  = serializers.CharField()

    def validate(self, data):
        if User.objects.filter(username = data['username']).exists():
            raise serializers.ValidationError("Username is already exits")
        if User.objects.filter(email = data['email']).exists():
            raise serializers.ValidationError("email is already registered")
        
        return data
    
    def create(self, validated_data):
        user = User.objects.create(first_name = validated_data['first_name'],
                                   last_name = validated_data['last_name'],
                                   username = validated_data['username'].lower(),
                                    email = validated_data['email']                                   
                                   )
        user.set_password(validated_data['password'])
        user.save()
        return validated_data


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()