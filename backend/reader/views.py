from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Reader
from .serializers import ReaderSerializer
from rest_framework.response import Response
#from rest_framework import statusLoginReaderSerializer

from rest_framework_simplejwt.tokens import RefreshToken

from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

# Lista e criação de leitores
class ReaderListCreateView(ListCreateAPIView):
    # Define o modelo
    queryset = Reader.objects.all()
    # Define o serializador
    serializer_class = ReaderSerializer
    
    # Define as permissões (apenas usuários autenticados podem acessar)
    #permission_classes = [IsAuthenticated]


# Recuperação, atualização e exclusão de leitores
class ReaderRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    # Define o modelo
    queryset = Reader.objects.all()
    # Define o serializador
    serializer_class = ReaderSerializer
    
    # Define as permissões (apenas usuários autenticados podem acessar)
    #permission_classes = [IsAuthenticated]
    
    
class ReaderObtainTokenView(APIView):
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

        return Response({'access_token': access_token})
    
class ReaderLogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        refresh_token = request.data.get("refresh_token")

        if not refresh_token:
            return Response({"error": "Refresh token is required."}, status=400)

        try:
            RefreshToken(refresh_token).blacklist()
            return Response({"message": "Logout successful."})
        except Exception as e:
            return Response({"error": str(e)}, status=500)