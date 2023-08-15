from rest_framework import serializers
from .models import MyClass

class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyClass
        fields = '__all__'
