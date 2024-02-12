from rest_framework import serializers
from .models import Producer


class ProducerSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
        model = Producer
        fields = '__all__'

# Atualizar produtor
class UpdateProducerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producer
        fields = ['cnpj', 'bank_name', 'bank_agency', 'number_account', 'account_type']
