from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    #id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, blank=True)
    username = models.CharField(max_length=20, unique=True, blank=True)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    password = models.CharField(max_length=16)
    email = models.CharField(unique=True, max_length=60)
    birthdate = models.DateTimeField()
    phone_number = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'user'