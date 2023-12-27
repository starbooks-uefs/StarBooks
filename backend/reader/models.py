from django.db import models
from django.contrib.auth import get_user_model

class Reader(get_user_model()):
    cpf = models.CharField(max_length=11, unique=True)
    gender = models.CharField(max_length=15, blank=True, null=True)
    cardholder = models.CharField(max_length=50)
    cvv = models.IntegerField()
    card_number = models.CharField(max_length=20)
    card_date = models.DateField()

    class Meta:
        #managed = False
        #proxy = True
        db_table = 'reader'