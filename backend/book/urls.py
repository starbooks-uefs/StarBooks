from django.urls import path
from .views import BookListCreateView, BookRetrieveUpdateDestroyView, AddBookView, UpdateBookPriceView, RemoveBookView

urlpatterns = [
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookRetrieveUpdateDestroyView.as_view(), name='book-retrieve-update-destroy'),
    path('add_book/', AddBookView.as_view(), name='add-book'),
    path('update_book_price/<int:pk>/', UpdateBookPriceView.as_view(), name='update-book-price'),
    path('remove_book/<int:pk>/', RemoveBookView.as_view(), name='remove-book'),
]
