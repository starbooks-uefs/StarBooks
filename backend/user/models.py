from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=25, blank=True)
    last_name = models.CharField(max_length=25, blank=True)
    email = models.CharField(unique=True, max_length=60)
    birthdate = models.DateField(blank=True, default='2001-01-01')
    phone_number = models.CharField(max_length=20, blank=True)
    
    class Meta:
        db_table = 'user'
        
    def __str__(self):
        return self.username