from django.urls import path
from .views import EbookListCreateView, EbookRetrieveUpdateDestroyView, AddEBookView, UpdateEBookPriceView

urlpatterns = [
    path('ebooks/', EbookListCreateView.as_view(), name='ebook-list-create'),
    path('ebooks/<int:pk>/', EbookRetrieveUpdateDestroyView.as_view(), name='ebook-retrieve-update-destroy'),
    path('add_ebook/', AddEBookView.as_view(), name='add-ebook'),
    path('update_ebook_price/<int:pk>/', UpdateEBookPriceView.as_view(), name='update-ebook-price'),
    
]
