from rest_framework import serializers
from .models import Producer

from django.contrib.auth.hashers import check_password

class ProducerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producer
        fields = '__all__'
        
class LoginProducerSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if email and password:
            user = authenticate(email=email, password=password)
            if user:
                #return {'email': user.email, 'password': user.password}  # Apenas retorne os dados necessários para autenticação
                return user
            else:
                raise serializers.ValidationError("Invalid credentials")
        else:
            raise serializers.ValidationError("Email and password are required")
        
    
def authenticate(email=None, password=None):
    User = Producer

    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return None

    if password == user.password:
        return user

    return None
