from django.db import models
from django.contrib.auth import get_user_model


class Admin(get_user_model()):
    class Meta:
        #managed = False
        db_table = 'admin'