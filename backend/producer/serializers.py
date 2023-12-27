from rest_framework import serializers
from .models import Producer

from django.contrib.auth.hashers import check_password

class ProducerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producer
        fields = '__all__'
