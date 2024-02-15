from rest_framework.generics import RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, get_object_or_404
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Cart
from .serializers import CreateCartSerializer, CartSerializer, CartBookSerializer
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_204_NO_CONTENT

class CreateCartView(CreateAPIView):
    serializer_class = CreateCartSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(id_reader=self.request.user)

class ClearCartView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        # Limpa o carrinho do usuário
        cart = Cart.objects.get(id_reader=request.user)
        cart.id_book.clear()
        return Response({"message": "Cart cleared successfully."}, status=HTTP_204_NO_CONTENT)

class RemoveBookFromCartView(UpdateAPIView):
    queryset = Cart.objects.all()
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        cart = get_object_or_404(Cart, id_reader=request.user)
        book_pk = kwargs.get('pk')
        cart.id_book.remove(book_pk)
        return Response({"message": "Book removed from cart successfully."}, status=HTTP_204_NO_CONTENT)

class RetrieveCartView(RetrieveAPIView):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        cart, _ = Cart.objects.get_or_create(id_reader=self.request.user)
        return cart

class AddToCartView(CreateAPIView):
    serializer_class = CartBookSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        cart, _ = Cart.objects.get_or_create(id_reader=self.request.user)
        book_ids = serializer.validated_data['id_book']
        cart.id_book.add(*book_ids)