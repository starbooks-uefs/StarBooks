from django.urls import path
from .views import BookByCurrentMonthView, BookListCreateView, BookRetrieveUpdateDestroyView, AddBookView, BookSearchView, UpdateBookPriceView, RemoveBookView, BookByAuthorView, BookByGenderView, BookSearchView

urlpatterns = [
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookRetrieveUpdateDestroyView.as_view(), name='book-retrieve-update-destroy'),
    path('add_book/', AddBookView.as_view(), name='add-book'),
    path('update_book_price/<int:pk>/', UpdateBookPriceView.as_view(), name='update-book-price'),
    path('remove_book/<int:pk>/', RemoveBookView.as_view(), name='remove-book'),
    path('books/retrieve/gender/<str:gender>/', BookByGenderView.as_view(), name='book-by-gender'),
    path('books/retrieve/author/<str:author>/', BookByAuthorView.as_view(), name='book-by-author'),
    path('books/current-month/', BookByCurrentMonthView.as_view(), name='book-by-current-month'),
    path('books/search/', BookSearchView.as_view(), name='book-search')
]
