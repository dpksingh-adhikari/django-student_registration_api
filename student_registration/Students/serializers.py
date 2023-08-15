from rest_framework import serializers
from Students.models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        Model = Student
        fields = '__all__'