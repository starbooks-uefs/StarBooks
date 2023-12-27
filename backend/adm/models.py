from django.db import models
from django.contrib.auth import get_user_model

class Admin(get_user_model()):
    class Meta:
        #managed = False
        #proxy = True
        db_table = 'admin'

    def save(self, *args, **kwargs):
        self.user_type = 'Admin'
        super().save(*args, **kwargs)