from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class AccountManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('O campo de e-mail deve ser definido')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

    def create_admin(self, email, password=None, **extra_fields):
        extra_fields.setdefault('user_type', 'Admin')
        return self.create_superuser(email, password, **extra_fields)

    def create_reader(self, email, password=None, **extra_fields):
        extra_fields.setdefault('user_type', 'Reader')
        return self.create_user(email, password, **extra_fields)
    
    def create_producer(self, email, password=None, **extra_fields):
        extra_fields.setdefault('user_type', 'Producer')
        return self.create_user(email, password, **extra_fields)

class Account(AbstractUser):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=20, unique=True, blank=True)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    password = models.CharField(max_length=16)
    email = models.CharField(unique=True, max_length=60)
    birthdate = models.DateField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    
    USER_TYPE_CHOICES = [
        ('Reader', 'Reader'),
        ('Producer', 'Producer'),
        ('Admin', 'Admin'),
        ('Account', 'Account')
    ]
    
    user_type = models.CharField(max_length=12, choices=USER_TYPE_CHOICES, default='Account')
    
    
    objects = AccountManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []
    class Meta:
        #managed = False
        db_table = 'account'