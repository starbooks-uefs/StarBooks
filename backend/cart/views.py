from rest_framework.generics import RetrieveAPIView, CreateAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Book  # Atualize para o caminho real do seu modelo Book
from .models import Reader  # Atualize para o caminho real do seu modelo Reader
from .models import Cart
from .serializers import CartSerializer

class GetCartView(RetrieveAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        # Obtém o carrinho do leitor autenticado
        return Cart.objects.get(id_reader=self.request.user)

class CreateCartView(CreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Cria um carrinho associado ao leitor autenticado
        serializer.save(id_reader=self.request.user)

class UpdateCartView(UpdateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        # Obtém o carrinho do leitor autenticado
        return Cart.objects.get(id_reader=self.request.user)