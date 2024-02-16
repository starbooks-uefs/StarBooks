from django.db import models
from django.contrib.auth import get_user_model

class Reader(get_user_model()):
    cpf = models.CharField(max_length=11, unique=True)
    gender = models.CharField(max_length=15, blank=True, null=True)
    cardholder = models.CharField(max_length=50, blank=True, null=True)
    cvv = models.IntegerField(blank=True, null=True)
    card_number = models.CharField(max_length=20, blank=True, null=True)
    card_date = models.DateField(blank=True, null=True)
    
    class Meta:
        #managed = False
        db_table = 'reader'