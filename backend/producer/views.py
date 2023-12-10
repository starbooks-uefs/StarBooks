from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Producer
from .serializers import ProducerSerializer, LoginProducerSerializer

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status

from rest_framework_simplejwt.tokens import RefreshToken

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

@api_view(['POST'])
@permission_classes([])
def producer_login(request):
    if request.method == 'POST':
        serializer = LoginProducerSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            
            # Criar token
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            
            # Utilize um serializer para converter o objeto Producer para um formato serializável
            credentials = {"email": user.email, "password": user.password}
            
            return Response({'message': 'Login successful', 'credentials': credentials, 'access_token': access_token}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response({'message': 'Invalid request method'}, status=status.HTTP_400_BAD_REQUEST)