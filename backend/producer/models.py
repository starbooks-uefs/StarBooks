from django.db import models
from django.contrib.auth import get_user_model

class Producer(get_user_model()):
    cnpj = models.CharField(max_length=14, unique=True)
    bank_name = models.CharField(max_length=25)
    bank_agency = models.IntegerField()
    number_account = models.IntegerField()
    account_type = models.CharField(max_length=10)

    class Meta:
        #managed = False
        #proxy = True
        db_table = 'producer'