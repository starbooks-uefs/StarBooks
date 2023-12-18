from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['name', 'gender','author', 'publisher', 'id_producer', 'edition', 'synopsis', 'pdf_url', 'price', 'pages_number', 'date',
                  'cover_url', 'rating', 'language', 'submission_status', 'submission_date']

# Atualizar Ebook
class UpdateBookPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['price']