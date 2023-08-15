from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from Students.models import Student
from Students.serializers import StudentSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication



# Create your views here.

class StudentListCreateView(APIView):
    def get(self, request):
        users = Student.objects.all()   
        serializer = StudentSerializer(users, many= True)
        return Response(serializer.data)
       
    
    def post(self, request):
        data = request.data
        serializer = StudentSerializer(data= data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({
                "data":serializer.data,
                "info":"user created"
            },status= status.HTTP_201_CREATED)
        

class StudentDetailView(APIView):

    permission_classes = [IsAuthenticated]
    authentication_classes =[TokenAuthentication]
    
    def get_object(self, id):
        try:
            return Student.objects.get(id = id)
        except Student.DoesNotExist:
            return None
        

    def get(self,request, id):
        user = self.get_object(id)
        if user is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = StudentSerializer(user)
        return Response(serializer.data)
    
    def put(self, request, id):
        user = self.get_object(id)
        if user is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = StudentSerializer(user , data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    


    def delete(self, request, id):
        user = self.get_object(id)
        if user is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        user.delete()
        return Response({
            "info":"User deleted"
        },status= status.HTTP_200_OK)