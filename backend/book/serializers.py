from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False, read_only=True)
    
    class Meta:
        model = Book
        fields = '__all__'
        
class BookOnCartSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Book
        fields = ['id', 'name', 'author', 'cover_url', 'price']

# Atualizar Ebook
class UpdateBookPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['price']