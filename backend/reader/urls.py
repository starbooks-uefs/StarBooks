from django.urls import path
from .views import ReaderListCreateView, ReaderRetrieveUpdateDestroyView, reader_login



# URLS que serão chamas no arquivo urls.py da pasta principal do projeto
urlpatterns = [
    path('readers/', ReaderListCreateView.as_view(), name='reader-list-create'),
    path('readers/<uuid:pk>/', ReaderRetrieveUpdateDestroyView.as_view(), name='reader-retrieve-update-destroy'),
    path('accounts/reader/login/', reader_login, name='reader-login'),
]