from django.db import models
from django.contrib.auth import get_user_model

class Producer(get_user_model()):
    cnpj = models.CharField(max_length=14, unique=True)
    bank_name = models.CharField(max_length=25)
    bank_agency = models.IntegerField()
    number_account = models.CharField(max_length=20)
    account_type = models.CharField(max_length=10)

    class Meta:
        #managed = False
        db_table = 'producer'