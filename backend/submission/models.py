from django.db import models
from adm.models import Admin
from book.models import Book


class Submission(models.Model):
    id_admin = models.OneToOneField(Admin, models.DO_NOTHING, db_column='id_admin', primary_key=True)  # The composite primary key (id_admin, id_book) found, that is not supported. The first column is selected.
    id_book = models.ForeignKey(Book, models.DO_NOTHING, db_column='id_book')

    class Meta:
        managed = False
        db_table = 'submission'
        unique_together = (('id_admin', 'id_book'),)
