# serializers.py
from rest_framework import serializers
from .models import Reader

class ReaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reader
        fields = '__all__'