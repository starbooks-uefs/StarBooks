from django.db import models

# Create your models here.
class Producer(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    password = models.CharField(max_length=16)
    email = models.CharField(unique=True, max_length=60)
    birthdate = models.DateTimeField()
    phone_number = models.IntegerField(blank=True, null=True)
    cnpj = models.IntegerField(unique=True)
    bank_name = models.CharField(max_length=25)
    bank_agency = models.IntegerField()
    number_account = models.IntegerField()
    account_type = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'producer'