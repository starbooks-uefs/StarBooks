from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Reader
from .serializers import ReaderSerializer
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework import status


# Lista e criação de leitores
class ReaderListCreateView(ListCreateAPIView):
    queryset = Reader.objects.all()
    serializer_class = ReaderSerializer
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