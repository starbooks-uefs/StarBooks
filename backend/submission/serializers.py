from rest_framework import serializers
from .models import Submission
from .models import Book


class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)    
    class Meta:
        model = Book
        fields = '__all__'