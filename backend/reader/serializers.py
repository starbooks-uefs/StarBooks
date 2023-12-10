from rest_framework import serializers
from .models import Reader

from django.contrib.auth.hashers import check_password

class ReaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reader
        fields = '__all__'
