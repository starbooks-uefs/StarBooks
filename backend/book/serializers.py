from rest_framework import serializers
from .models import Ebook

class EbookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ebook
        fields = '__all__'
