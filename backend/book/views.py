import datetime
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView, UpdateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import DestroyAPIView
from .models import Book
from .serializers import BookSerializer, UpdateBookPriceSerializer
from .permissions import IsBookOwner
from rest_framework.response import Response
from rest_framework import status
from submission.models import Submission
from django.shortcuts import get_object_or_404

from django.urls import path



class BookListCreateView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # permission_classes = [IsAuthenticated]

class BookRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    #permission_classes = [IsAuthenticated]
    
    def delete(self, request, *args, **kwargs):
        # Obtém o ID do livro a ser excluído
        book_id = kwargs.get('pk')
        
        # Verifica se o livro existe
        book_instance = get_object_or_404(Book, pk=book_id)
        
        # Verifica se existem submissões associadas ao livro
        if Submission.objects.filter(id_book=book_instance).exists():
            # Se houver submissões, você pode optar por excluí-las ou atualizá-las
            # Aqui, estou excluindo todas as submissões associadas ao livro
            Submission.objects.filter(id_book=book_instance).delete()
            # Ou você pode atualizar as submissões para remover a referência ao livro
            # Submission.objects.filter(id_book=book_instance).update(id_book=None)
        
        # Exclui o livro
        book_instance.delete()

        return Response({"message": "Book deleted successfully."}, status=status.HTTP_204_NO_CONTENT)

class AddBookView(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    #permission_classes = [IsAuthenticated]


class UpdateBookPriceView(UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = UpdateBookPriceSerializer
    #permission_classes = [IsAuthenticated, IsBookOwner]


class RemoveBookView(DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "Livro removido com sucesso."}, status=status.HTTP_204_NO_CONTENT)
    # permission_classes = [IsAuthenticated, IsBookOwner]


class BookByGenderView(ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        gender = self.kwargs['gender']
        return Book.objects.filter(gender=gender)

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def handle_exception(self, exc):
        if 'gender' not in self.kwargs:
            return Response({'error': 'O parâmetro "gender" é obrigatório na URL.'}, status=status.HTTP_400_BAD_REQUEST)
        return super().handle_exception(exc)

class BookByAuthorView(ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        author = self.kwargs['author']
        return Book.objects.filter(author=author)

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def handle_exception(self, exc):
        if 'author' not in self.kwargs:
            return Response({'error': 'O parâmetro "author" é obrigatório na URL.'}, status=status.HTTP_400_BAD_REQUEST)
        return super().handle_exception(exc)
    
class BookByCurrentMonthView(ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        if getattr(datetime, 'now', None):
            current_year = datetime.now().current_year
            current_month = datetime.now().current_month
        else:
            current_year = datetime.datetime.now().year
            current_month = datetime.datetime.now().month
        
        # Filter books published in the current month
        queryset = Book.objects.filter(date__year=current_year, date__month=current_month)
        return queryset
    
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def handle_exception(self, exc):
        return super().handle_exception(exc)
    

class BookSearchView(ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = Book.objects.all()

        # Obter parâmetros de consulta da solicitação
        name = self.request.query_params.get('name', None)
        author = self.request.query_params.get('author', None)
        year = self.request.query_params.get('year', None)
        gender = self.request.query_params.get('gender', None)
        publisher = self.request.query_params.get('publisher', None)

        # Aplicar filtros com base nos parâmetros de consulta
        if name:
            queryset = queryset.filter(name__icontains=name)
        if author:
            queryset = queryset.filter(author__icontains=author)
        if year:
            queryset = queryset.filter(date__year=year)
        if gender:
            queryset = queryset.filter(gender__icontains=gender)
        if publisher:
            queryset = queryset.filter(publisher__icontains=publisher)

        return queryset

class BookListByProducerID(ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        id_producer = self.kwargs.get('pk')
        queryset = Book.objects.filter(id_producer=id_producer)
        return queryset