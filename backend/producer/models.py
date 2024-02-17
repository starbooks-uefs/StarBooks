from django.db import models
from django.contrib.auth import get_user_model

class Producer(get_user_model()):
    cnpj = models.CharField(max_length=14, unique=True)
    bank_name = models.CharField(max_length=25, blank=True, null=True)
    bank_agency = models.IntegerField(blank=True, null=True)
    number_account = models.CharField(max_length=20, blank=True, null=True)
    account_type = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'producer'