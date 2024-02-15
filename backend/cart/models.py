# models.py
from django.db import models
from reader.models import Reader
from book.models import Book

class Cart(models.Model):
    id_reader = models.OneToOneField(Reader, on_delete=models.CASCADE, db_column='id_reader')
    id_book = models.ManyToManyField(Book, blank=True, db_column='id_book')

    class Meta:
        db_table = 'cart'
        unique_together = ('id_reader',)
