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
        
class Cart(models.Model):
    id_book = models.OneToOneField(Book, models.DO_NOTHING, db_column='id_book', primary_key=True)  # The composite primary key (id_book, id_reader) found, that is not supported. The first column is selected.
    id_reader = models.ForeignKey('Reader', models.DO_NOTHING, db_column='id_reader')

    class Meta:
        managed = False
        db_table = 'cart'
        unique_together = (('id_book', 'id_reader'),)
        
class Reader(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    password = models.CharField(max_length=16)
    email = models.CharField(unique=True, max_length=60)
    birthdate = models.DateTimeField()
    phone_number = models.IntegerField(blank=True, null=True)
    cpf = models.IntegerField(unique=True)
    gender = models.CharField(max_length=15, blank=True, null=True)
    cardholder = models.CharField(max_length=50)
    cvv = models.IntegerField()
    card_number = models.IntegerField()
    card_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'reader'