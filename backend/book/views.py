from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import DestroyAPIView
from .models import Book
from .serializers import BookSerializer, UpdateBookPriceSerializer
from .permissions import IsBookOwner


class BookListCreateView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class AddBookView(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Atribuir o e-book ao produtor atual
        serializer.save(producer=self.request.user.producer_profile)

class UpdateBookPriceView(UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = UpdateBookPriceSerializer
    permission_classes = [IsAuthenticated, IsBookOwner]

    def perform_update(self, serializer):
        serializer.save()

class RemoveBookView(DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated, IsBookOwner]