import datetime
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView, UpdateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import DestroyAPIView
from .models import Book
from .serializers import BookSerializer, UpdateBookPriceSerializer
from .permissions import IsBookOwner
from rest_framework.response import Response
from rest_framework import status

from django.urls import path



class BookListCreateView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # permission_classes = [IsAuthenticated]

class BookRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    #permission_classes = [IsAuthenticated]

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
    