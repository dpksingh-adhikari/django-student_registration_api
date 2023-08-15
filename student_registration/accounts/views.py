from django.shortcuts import render
from accounts.serializers import LoginSerializer ,RegisterSerializer
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate


# Create your views here.

class RegisterView(APIView):
    def post(self, request):
        data = request.data
        serializer = RegisterSerializer(data=data)

        if not serializer.is_valid():
            return Response({
                'data':serializer.errors,
                "info":"something went wrong"
            }, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response({
            "data":serializer.data,
            "info":"user created successfully"
        }, status= status.HTTP_201_CREATED)
    
    def get(self, request):
        obj = User.objects.all()
        serializer = RegisterSerializer(obj, many  = True)
        return Response(serializer.data)
    

    def delete(self, request, id):
        obj = User(id)
        obj.delete()
        return Response({"info":"user deleted successfully"})
    

class LoginView(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = LoginSerializer(data= data)

            if not serializer.is_valid():
                return Response({
                    "data":serializer.errors,
                    "info":"something went wrong"
                } , status= status.HTTP_400_BAD_REQUEST)
            
            user = authenticate(username = serializer.data['username'] , password = serializer.data['password'])

            if not user:
                return Response({
                    "data":{},
                    "info":"invalid credential"
                })

            token,_ = Token.objects.get_or_create(user = user)
            return Response({
                "info":"user logged in",
                "token":str(token)
            })
        except Exception as e:
            print(e)
        return Response ({
                "data":{},
                "info":"something went wrong"
            })
            