from django.db import models

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

class Book(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=20)
    publisher = models.CharField(max_length=20, blank=True, null=True)
    id_producer = models.ForeignKey('Producer', models.DO_NOTHING, db_column='id_producer')
    edition = models.IntegerField()
    synopsis = models.TextField()
    pdf_url = models.CharField(max_length=255)
    price = models.FloatField()
    pages_number = models.IntegerField()
    date = models.DateTimeField()
    cover_url = models.CharField(max_length=255)
    rating = models.IntegerField(blank=True, null=True)
    language = models.CharField(max_length=25, blank=True, null=True)
    submission_status = models.BooleanField()
    submission_date = models.DateTimeField()
    submission_reason = models.TextField()

    class Meta:
        managed = False
        db_table = 'book'