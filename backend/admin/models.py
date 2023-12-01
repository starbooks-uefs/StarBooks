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



