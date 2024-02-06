from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=25, blank=True)
    last_name = models.CharField(max_length=25, blank=True)
    email = models.CharField(unique=True, max_length=60)
    birthdate = models.DateField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    
    class Meta:
        db_table = 'user'