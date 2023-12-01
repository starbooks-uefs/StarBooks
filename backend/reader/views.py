from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Reader
from .serializers import ReaderSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
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
