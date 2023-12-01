# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Admin(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    password = models.CharField(max_length=16)
    email = models.CharField(unique=True, max_length=60)
    birthdate = models.DateTimeField()
    phone_number = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admin'


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


class Purchase(models.Model):
    id_book = models.OneToOneField(Book, models.DO_NOTHING, db_column='id_book', primary_key=True)  # The composite primary key (id_book, id_reader) found, that is not supported. The first column is selected.
    id_reader = models.ForeignKey('Reader', models.DO_NOTHING, db_column='id_reader')
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'purchase'
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


class Submission(models.Model):
    id_admin = models.OneToOneField(Admin, models.DO_NOTHING, db_column='id_admin', primary_key=True)  # The composite primary key (id_admin, id_book) found, that is not supported. The first column is selected.
    id_book = models.ForeignKey(Book, models.DO_NOTHING, db_column='id_book')

    class Meta:
        managed = False
        db_table = 'submission'
        unique_together = (('id_admin', 'id_book'),)
