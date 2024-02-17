from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Submission
from producer.models import Producer
from book.models import Book, SubmissionStatus
from .serializers import SubmissionSerializer, BookSerializer, BookSubmissionSerializer
from rest_framework.permissions import IsAuthenticated
from adm.models import Admin
from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import Submission

class SubmissionListCreateView(ListCreateAPIView):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer
    #permission_classes = [IsAuthenticated]

class SubmissionRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer
    #permission_classes = [IsAuthenticated]

class BookSubmissionView(APIView):
    def post(self, request, *args, **kwargs):
        # Obtenha o usuário autenticado
        username = self.request.user
        # Obtenha ou crie o produtor associado ao usuário
        producer, created = Producer.objects.get_or_create(username=username)
        # Serialize os dados recebidos para criar um novo livro
        serializer = BookSubmissionSerializer(data=request.data)
        if serializer.is_valid():
            # Obtenha o ID do produtor
            producer_id = producer.id
            # Atribua o produtor ao campo id_producer do serializer
            serializer.validated_data['id_producer'] = producer
            # Crie o livro associado ao produtor
            book = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AdminSubmissionsListView(ListAPIView):
    serializer_class = SubmissionSerializer
    #permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Obtém o ID do administrador a partir dos parâmetros da URL
        id_admin = self.kwargs.get('id_admin')
        
        # Retorna todas as submissões associadas ao administrador com o ID especificado
        return Submission.objects.filter(id_admin=id_admin)
    
    

class ApproveSubmissionView(APIView):
    def put(self, request, pk, format=None):
        try:
            book = Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return Response({"message": "Book does not exist"}, status=status.HTTP_404_NOT_FOUND)

        book.submission_status = SubmissionStatus.approved
        book.submission_reason = ''  # Limpar o submission_reason
        book.save()

        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)


class DisapproveSubmissionView(APIView):
    def put(self, request, pk, format=None):
        try:
            book = Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return Response({"message": "Book does not exist"}, status=status.HTTP_404_NOT_FOUND)

        submission_reason = request.data.get('submission_reason', None)
        if submission_reason is None:
            return Response({"message": "Submission reason is required"}, status=status.HTTP_400_BAD_REQUEST)

        book.submission_status = SubmissionStatus.disapproved
        book.submission_reason = submission_reason
        book.save()

        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)