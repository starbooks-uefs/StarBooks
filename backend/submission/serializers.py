from rest_framework import serializers
from .models import Submission
from .models import Book
from producer.models import Producer


class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)  
    class Meta:
        model = Book
        fields = '__all__'
        
class BookSubmissionSerializer(serializers.ModelSerializer):
    id_producer = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Book
        fields = '__all__'