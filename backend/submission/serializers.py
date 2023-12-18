from rest_framework import serializers
from .models import Submission


class serializeSubmission(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = '__all__'
