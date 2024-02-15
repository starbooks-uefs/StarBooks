from rest_framework import serializers
from .models import Producer
from django.contrib.auth.models import User



class ProducerSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
        model = Producer
        fields = '__all__'

# Atualizar produtor
class UpdateProducerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Producer
        fields = ['cnpj', 'bank_name', 'bank_agency', 'number_account', 'account_type',
                  'username', 'first_name', 'last_name', 'email', 'birthdate', 'phone_number']    
    
