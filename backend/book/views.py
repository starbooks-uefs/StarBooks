from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Ebook
from .serializers import EbookSerializer, UpdateEBookPriceSerializer
from .permissions import IsEBookOwner

class EbookListCreateView(ListCreateAPIView):
    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer
    permission_classes = [IsAuthenticated]

class EbookRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer
    permission_classes = [IsAuthenticated]

class AddEBookView(CreateAPIView):
    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Atribuir o e-book ao produtor atual
        serializer.save(producer=self.request.user.producer_profile)

class UpdateEBookPriceView(UpdateAPIView):
    queryset = Ebook.objects.all()
    serializer_class = UpdateEBookPriceSerializer
    permission_classes = [IsAuthenticated, IsEBookOwner]

    def perform_update(self, serializer):
        serializer.save()
