from django.db import models
from classes.models import MyClass
from django.contrib.auth import get_user_model

User = get_user_model()

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True)
    date_of_birth = models.DateField()
    gender_choice = (
        ("male", "Male"),
        ("Female", "Female"),
    )
    gender = models.CharField(choices=gender_choice, max_length=10)
    status = models.BooleanField(default=False)
    image = models.ImageField(upload_to='profile_images/')
    student_class = models.ForeignKey(MyClass, on_delete=models.CASCADE)


    USERNAME_FIELD = 'phone' 

    def __str__(self):
        return self.phone