from django.db import models
from django.contrib.auth import get_user_model

class Reader(get_user_model()):
    cpf = models.IntegerField(unique=True)
    gender = models.CharField(max_length=15, blank=True, null=True)
    cardholder = models.CharField(max_length=50)
    cvv = models.IntegerField()
    card_number = models.IntegerField()
    card_date = models.DateTimeField()

    class Meta:
        db_table = 'reader'