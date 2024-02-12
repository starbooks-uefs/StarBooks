from rest_framework import serializers
from .models import User

class UserEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'birthdate', 'phone_number']

        