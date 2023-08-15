from rest_framework import generics
from .models import MyClass
from .serializers import ClassSerializer

class ClassCreateView(generics.CreateAPIView):
    queryset = MyClass.objects.all()
    serializer_class = ClassSerializer