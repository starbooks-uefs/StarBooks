# models.py
from django.db import models
from reader.models import Reader
from book.models import Book

class Cart(models.Model):
    id_reader = models.OneToOneField(Reader, on_delete=models.CASCADE, primary_key=True, db_column='id_reader')
    id_book = models.OneToOneField(Book, on_delete=models.CASCADE, null=True, blank=True, db_column='id_book')

    class Meta:
        #managed = False
        db_table = 'cart'
