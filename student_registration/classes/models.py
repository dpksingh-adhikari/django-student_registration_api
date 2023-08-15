from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class MyClass(models.Model):
    CLASS_CHOICES = (
        ('Fifth', 'Fifth'),
        ('Sixth', 'Sixth'),
        ('Seventh', 'Seventh'),
        ('Eighth', 'Eighth'),
        ('Ninth', 'Ninth'),
        ('Tenth', 'Tenth'),
        ('Eleventh', 'Eleventh'),
        ('Twelfth', 'Twelfth'),
    )

    class_name = models.CharField(max_length=10, choices= CLASS_CHOICES)


    def __str__(self) -> str:
        return self.class_name