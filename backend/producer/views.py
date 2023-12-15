from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Producer
from .serializers import ProducerSerializer
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework import status


class ProducerListCreateView(ListCreateAPIView):
    queryset = Producer.objects.all()
    serializer_class = ProducerSerializer
    # Define as permissões (apenas usuários autenticados podem acessar)
    #permission_classes = [IsAuthenticated]

class ProducerRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Producer.objects.all()
    serializer_class = ProducerSerializer
    # Define as permissões (apenas usuários autenticados podem acessar)
    #permission_classes = [IsAuthenticated]

class ProducerLoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')

        try:
            user = Producer.objects.get(email=email, password=password)
        except Producer.DoesNotExist:
            return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)

        return Response({'access_token': access_token, 'refresh_token': refresh_token},status=status.HTTP_200_OK)
    
class ProducerLogoutView(APIView):
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