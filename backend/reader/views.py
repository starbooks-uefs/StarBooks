from rest_framework.decorators import api_view, permission_classes
from rest_framework.status import HTTP_201_CREATED
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Reader
from book.models import Book
from book.serializers import BookSerializer
from purchase.models import Purchase
from purchase.serializers import PurchaseSerializer
from .serializers import ReaderSerializer
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework import status
from django.utils import timezone
from django.shortcuts import get_object_or_404
from cart.models import Cart
# Lista e criação de leitores
class ReaderListCreateView(ListCreateAPIView):
    queryset = Reader.objects.all()
    serializer_class = ReaderSerializer
    
    def perform_create(self, serializer):
        # Cria o novo leitor
        reader_instance = serializer.save()

        # Cria um carrinho associado ao novo leitor
        Cart.objects.create(id_reader=reader_instance)

        return Response(serializer.data, status=HTTP_201_CREATED)
    
    # Define as permissões (apenas usuários autenticados podem acessar)
    #permission_classes = [IsAuthenticated]


# Recuperação, atualização e exclusão de leitores
class ReaderRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Reader.objects.all()
    serializer_class = ReaderSerializer
    
    # Define as permissões (apenas usuários autenticados podem acessar)
    #permission_classes = [IsAuthenticated]
    
    
class ReaderLoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')

        try:
            user = Reader.objects.get(email=email, password=password)
        except Reader.DoesNotExist:
            return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)

        return Response({'access_token': access_token, 'refresh_token': refresh_token},status=status.HTTP_200_OK)
    
class ReaderLogoutView(APIView):
    #permission_classes = [IsAuthenticated]

    def post(self, request):
        refresh_token = request.data.get("refresh_token")

        if not refresh_token:
            return Response({"error": "Refresh token is required."})

        try:
            RefreshToken(refresh_token).blacklist()
            return Response({"message": "Logout successful."}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=500)
        
        
class ReaderAddPurchaseToLibraryView(APIView):
    serializer_class = PurchaseSerializer
    
    def post(self, request, *args, **kwargs):
        id_book = request.data.get('id_book')
        id_reader = request.data.get('id_reader')

        # Buscar as instâncias do livro e do leitor
        book_instance = get_object_or_404(Book, id=id_book)
        reader_instance = get_object_or_404(Reader, id=id_reader)

        # Verificar se o livro já está na biblioteca do leitor
        existing_purchase = Purchase.objects.filter(id_book=book_instance, id_reader=reader_instance).exists()

        if existing_purchase:
            return Response({'error': 'Este livro já está na sua biblioteca.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Criar a compra usando as instâncias do livro e do leitor
            purchase = Purchase.objects.create(
                id_book=book_instance,
                id_reader=reader_instance,
                date=timezone.now()
            )
            serializer = PurchaseSerializer(purchase)
            return Response({"Compra efetuada com sucesso!": serializer.data}, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        

class ReaderPurchasesView(ListAPIView):
    serializer_class = PurchaseSerializer

    def get_queryset(self):
        id_reader = self.kwargs['id_reader']
        user = get_object_or_404(Reader, pk=id_reader)
        purchases = Purchase.objects.filter(id_reader=user.id)
        return purchases

class ReaderPurchaseDetailView(RetrieveAPIView):
    serializer_class = PurchaseSerializer

    def get_object(self):
        id_reader = self.kwargs['id_reader']
        id_purchase = self.kwargs['id_purchase']
        purchase = get_object_or_404(Purchase, id_reader=id_reader, pk=id_purchase)
        return purchase
    
class ReaderBooksView(ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        id_reader = self.kwargs['id_reader']
        user = get_object_or_404(Reader, pk=id_reader)
        purchases = Purchase.objects.filter(id_reader=user.id)
        books = [purchase.id_book for purchase in purchases]
        return books

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)