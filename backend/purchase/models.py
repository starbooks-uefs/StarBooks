from django.db import models
from book.models import Book
from reader.models import Reader

class Purchase(models.Model):
    id = models.AutoField(primary_key=True)
    id_book = models.ForeignKey(Book, on_delete=models.CASCADE, db_column='id_book')
    id_reader = models.ForeignKey(Reader, on_delete=models.CASCADE, db_column='id_reader')
    date = models.DateTimeField()

    class Meta:
        #managed = False
        db_table = 'purchase'
        unique_together = (('id_book', 'id_reader'),)
    
    def __str__(self):
        return f'Compra do usuário "{self.id_reader}" do livro "{self.id_book}"'