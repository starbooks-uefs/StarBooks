from django.db import models
from producer.models import Producer

from enumchoicefield import ChoiceEnum, EnumChoiceField

class SubmissionStatus(ChoiceEnum):
    approved = "Aprovado"
    disapproved = "Reprovado"
    pending = "Pendente"


class Book(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    gender = models.TextField()
    publisher = models.CharField(max_length=20, blank=True, null=True)
    id_producer = models.ForeignKey(Producer, models.DO_NOTHING, db_column='id_producer')
    edition = models.IntegerField()
    synopsis = models.TextField()
    pdf_url = models.CharField(max_length=255)
    price = models.FloatField()
    pages_number = models.IntegerField()
    date = models.DateField()
    cover_url = models.CharField(max_length=255)
    rating = models.IntegerField(blank=True, null=True)
    language = models.CharField(max_length=25, blank=True, null=True)
    submission_status = EnumChoiceField(SubmissionStatus, default=SubmissionStatus.pending)
    submission_date = models.DateTimeField(auto_now_add=True, blank=True)
    submission_reason = models.TextField(null=True, blank=True, default=None)

    class Meta:
        #managed = False
        db_table = 'book'