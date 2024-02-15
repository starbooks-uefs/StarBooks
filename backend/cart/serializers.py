from rest_framework import serializers
from .models import Cart
from book.serializers import BookOnCartSerializer

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'
        

class CartRetrieveSerializer(serializers.ModelSerializer):
    id_book = BookOnCartSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ['id_reader', 'id_book']
                
class CartBookSerializer(serializers.ModelSerializer):
    id_book = BookOnCartSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ['id_book']

class CreateCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = []  # Nenhum campo especificado