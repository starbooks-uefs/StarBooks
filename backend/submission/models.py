from django.db import models
from adm.models import Admin
from producer.models import Producer
from book.models import Book


class Submission(models.Model):

    data = models.DateField(default="")
    motivo = models.CharField(max_length=25,default='')
    status = models.CharField(max_length=25,default='')
    id_book = models.ForeignKey(Book, on_delete=models.CASCADE,default=None)
    id_Adm = models.ForeignKey(Admin, on_delete=models.DO_NOTHING,default=None)
    id_producer = models.ForeignKey(Producer, on_delete=models.DO_NOTHING,default=None)
    
    class Meta:
        managed = False
        db_table = 'submission'
