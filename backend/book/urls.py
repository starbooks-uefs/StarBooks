from django.urls import path
from .views import EbookListCreateView, EbookRetrieveUpdateDestroyView

urlpatterns = [
    path('ebooks/', EbookListCreateView.as_view(), name='ebook-list-create'),
    path('ebooks/<int:pk>/', EbookRetrieveUpdateDestroyView.as_view(), name='ebook-retrieve-update-destroy'),
    
]
