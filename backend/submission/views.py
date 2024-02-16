from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Submission
from book.models import Book, SubmissionStatus
from .serializers import SubmissionSerializer, BookSerializer
from rest_framework.permissions import IsAuthenticated
from adm.models import Admin

class SubmissionListCreateView(ListCreateAPIView):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer
    #permission_classes = [IsAuthenticated]

class SubmissionRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer
    #permission_classes = [IsAuthenticated]

class BookSubmissionView(APIView):
    def post(self, request, *args, **kwargs):
        # Serialize os dados recebidos para criar um novo livro
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            # Cria o livro
            book = serializer.save()

            admin = Admin.objects.first()  # Atribui a submissão ao primeiro admin

            # Cria a submissão associada ao admin
            submission = Submission.objects.create(id_admin=admin, id_book=book)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AdminSubmissionsListView(ListAPIView):
    serializer_class = SubmissionSerializer
    #permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Obtém o ID do administrador a partir dos parâmetros da URL
        id_admin = self.kwargs.get('id_admin')
        
        # Retorna todas as submissões associadas ao administrador com o ID especificado
        return Submission.objects.filter(id_admin=id_admin)
    
    

class ApproveSubmissionView(APIView):
    def put(self, request, pk, format=None):
        try:
            book = Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return Response({"message": "Book does not exist"}, status=status.HTTP_404_NOT_FOUND)

        book.submission_status = SubmissionStatus.approved
        book.submission_reason = ''  # Limpar o submission_reason
        book.save()

        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)


class DisapproveSubmissionView(APIView):
    def put(self, request, pk, format=None):
        try:
            book = Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return Response({"message": "Book does not exist"}, status=status.HTTP_404_NOT_FOUND)

        submission_reason = request.data.get('submission_reason', None)
        if submission_reason is None:
            return Response({"message": "Submission reason is required"}, status=status.HTTP_400_BAD_REQUEST)

        book.submission_status = SubmissionStatus.disapproved
        book.submission_reason = submission_reason
        book.save()

        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)