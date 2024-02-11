from rest_framework import serializers
from .models import Cart

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'
        
class CartBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id_book']