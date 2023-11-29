from django.db import models
import uuid

from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.utils.translation import gettext_lazy as _

# Usuario base que possui todas as informações em comum dos outros usuarios
class BaseUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    password = models.CharField(max_length=16)
    email = models.EmailField(max_length=60, unique=True)
    birthdate = models.DateField()
    phone_number = models.IntegerField(null=True, blank=True)
    # Campos comuns #

    class Meta:
        abstract = True

class Reader(BaseUser):
    cpf = models.IntegerField(unique=True)
    gender = models.CharField(max_length=15, null=True, blank=True)
    cardholder = models.CharField(max_length=50)
    cvv = models.IntegerField()
    card_number = models.IntegerField()
    card_date = models.DateTimeField()

    # Adicione o argumento related_name para evitar conflitos
    groups = models.ManyToManyField(Group, related_name='reader_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='reader_user_permissions')
''' 
class Producer(BaseUser):
    cnpj = models.IntegerField(unique=True)
    bank_name = models.CharField(max_length=25)
    bank_agency = models.IntegerField()
    number_account = models.IntegerField()
    account_type = models.CharField(max_length=10)

class Admin(BaseUser):
    # Campos adicionais específicos para Admin, se necessário
    pass
''' 

