from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import DestroyAPIView
from .models import Book
from .serializers import BookSerializer, UpdateBookPriceSerializer
from .permissions import IsBookOwner
from rest_framework.response import Response
from rest_framework import status
from django_filters import FilterSet, CharFilter

class BookListCreateView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
   # permission_classes = [IsAuthenticated]

class BookListAPIView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

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
    

