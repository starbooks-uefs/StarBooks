from rest_framework import serializers
from .models import book

class EbookSerializer(serializers.ModelSerializer):
    class Meta:
        model = book
        fields = '__all__'

# Atualizar Ebook
class UpdateEBookPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = book
        fields = ['price']