from django.db import models
from django.contrib.auth.models import AbstractUser
from accounts.manager import UserManager

# Create your models here.

class CustomUser(AbstractUser):
    username = None
    phone_number = models.CharField(max_length=100, unique= True)
    email = models.EmailField()
    user_bio = models.CharField(max_length=100)


    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []
    objects = UserManager()