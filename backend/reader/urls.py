from django.urls import path
from .views import ReaderListCreateView, ReaderRetrieveUpdateDestroyView



# URLS que serão chamas no arquivo urls.py da pasta principal do projeto
urlpatterns = [
    
    path('api/readers/', ReaderListCreateView.as_view(), name='reader-list-create'),
    path('api/readers/<uuid:pk>/', ReaderRetrieveUpdateDestroyView.as_view(), name='reader-retrieve-update-destroy'),
    
    #path('api/teste1/', views.reader_list, name='teste1'),
    #path('api/teste2/<uuid:pk>/', views.reader_list, name='teste2'),
]