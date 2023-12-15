from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=50, blank=True)
    username = models.CharField(max_length=20, unique=True, blank=True)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    password = models.CharField(max_length=16)
    email = models.CharField(unique=True, max_length=60)
    birthdate = models.DateField()
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    
    USER_TYPE_CHOICES = [
        ('Reader', 'Reader'),
        ('Producer', 'Producer'),
        ('Admin', 'Admin'),
        ('User', 'User')
    ]
    
    user_type = models.CharField(max_length=12, choices=USER_TYPE_CHOICES)
    
    
    def save(self, *args, **kwargs):
        # Define is_staff e is_superuser com base no tipo de usuário
        if self.user_type == 'Admin' or self.user_type == 'User':
            self.is_staff = True
            self.is_superuser = True
        else:
            self.is_staff = False
            self.is_superuser = False

        super().save(*args, **kwargs)

    class Meta:
        #managed = False
        db_table = 'user'