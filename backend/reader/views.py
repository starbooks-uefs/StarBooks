from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Reader
from .serializers import ReaderSerializer, LoginReaderSerializer

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status

from rest_framework_simplejwt.tokens import RefreshToken

# Lista e criação de leitores
'''
ReaderListCreateView é uma classe de visualização genérica que lida
com operações de lista (GET) e criação (POST) para a entidade Reader.

Configuramos o queryset para todos os objetos Reader e o serializer_class para o ReaderSerializer que criamos anteriormente. 
'''
class ReaderListCreateView(ListCreateAPIView):
    # Define o modelo
    queryset = Reader.objects.all()
    # Define o serializador
    serializer_class = ReaderSerializer
    
    # Define as permissões (apenas usuários autenticados podem acessar)
    #permission_classes = [IsAuthenticated]


# Recuperação, atualização e exclusão de leitores
'''
ReaderRetrieveUpdateDestroyView é outra classe de visualização genérica que lida
com operações de recuperação (GET), atualização (PUT), destruição (DELETE) para a entidade Reader.
'''
class ReaderRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    # Define o modelo
    queryset = Reader.objects.all()
    # Define o serializador
    serializer_class = ReaderSerializer
    
    # Define as permissões (apenas usuários autenticados podem acessar)
    #permission_classes = [IsAuthenticated]

# Maneira 2 com apiview
@api_view(['GET', 'POST'])
def reader_list(request):
    if request.method == 'GET':
        readers = Reader.objects.all()
        serializer = ReaderSerializer(readers, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ReaderSerializer(data=request.data)
        if serializer.is_valid(): # se o serializer for valido
            serializer.save() # salva o objeto
            return Response(serializer.data, status=status.HTTP_201_CREATED) # retorna o objeto criado
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([])
def reader_login(request):
    if request.method == 'POST':
        serializer = LoginReaderSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            
            # Criar token
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            
            # Utilize um serializer para converter o objeto Reader para um formato serializável
            credentials = {"email": user.email, "password": user.password}
            
            return Response({'message': 'Login successful', 'credentials': credentials, 'access_token': access_token}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response({'message': 'Invalid request method'}, status=status.HTTP_400_BAD_REQUEST)

