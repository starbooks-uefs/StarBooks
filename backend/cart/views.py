from rest_framework.generics import RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, get_object_or_404
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Cart
from reader.models import Reader
from book.models import Book
from .serializers import CreateCartSerializer, CartBookSerializer, CartRetrieveSerializer
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_204_NO_CONTENT
from rest_framework.exceptions import ValidationError
from rest_framework import status



class CreateCartView(CreateAPIView):
    serializer_class = CreateCartSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Obtém o leitor associado ao usuário autenticado
        reader = Reader.objects.filter(username=self.request.user).first()
        
        if reader is None:
            raise ValidationError("Could not find the reader associated with the user.")
        
        # Verifica se já existe um carrinho para o leitor
        if Cart.objects.filter(id_reader=reader).exists():
            raise ValidationError("A cart already exists for this reader.")
        
        # Cria um novo carrinho associado ao leitor
        serializer.save(id_reader=reader)

class ClearCartView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        # Limpa o carrinho do usuário
        cart = Cart.objects.get(id_reader=request.user.id)
        cart.id_book.clear()
        return Response({"message": "Cart cleared successfully."}, status=HTTP_204_NO_CONTENT)

class RemoveBookFromCartView(UpdateAPIView):
    queryset = Cart.objects.all()
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        cart = get_object_or_404(Cart, id_reader=request.user.id)
        book_pk = kwargs.get('pk')
        cart.id_book.remove(book_pk)
        return Response({"message": "Book removed from cart successfully."}, status=HTTP_204_NO_CONTENT)

class RetrieveCartView(RetrieveAPIView):
    serializer_class = CartRetrieveSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        username = self.request.user
        reader_instance, _ = Reader.objects.get_or_create(username=username)
        cart, _ = Cart.objects.get_or_create(id_reader=reader_instance)
        return cart


class AddToCartView(CreateAPIView):
    serializer_class = CartBookSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Obtém o id_book da URL
        id_book = self.kwargs.get('id_book')
        # Obtém a instância do livro ou retorna 404 se não existir
        book_instance = get_object_or_404(Book, id=id_book)
        # Adiciona a instância do livro ao serializer do carrinho
        serializer.validated_data['id_book'] = [book_instance]
        # Obtém ou cria o carrinho do usuário autenticado
        cart, _ = Cart.objects.get_or_create(id_reader=self.request.user)
        # Adiciona o livro ao carrinho
        cart.id_book.add(book_instance)
        # Retorna uma resposta de sucesso
        return Response({'message': 'Book added to cart successfully'}, status=status.HTTP_201_CREATED)