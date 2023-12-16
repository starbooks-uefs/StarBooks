from django.db import models
from producer.models import Producer

class Book(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=20)
    publisher = models.CharField(max_length=20, blank=True, null=True)
    id_producer = models.ForeignKey(Producer, models.DO_NOTHING, db_column='id_producer')
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
      #  managed = False
        db_table = 'book'