from django.urls import path
from .views import ReaderListCreateView, ReaderRetrieveUpdateDestroyView, ReaderLoginView, ReaderLogoutView



# URLS que serão chamas no arquivo urls.py da pasta principal do projeto
urlpatterns = [
    path('readers/', ReaderListCreateView.as_view(), name='reader-list-create'),
    path('readers/<uuid:pk>/', ReaderRetrieveUpdateDestroyView.as_view(), name='reader-retrieve-update-destroy'),
    path('readers/login/', ReaderLoginView.as_view(), name='reader-login'),
    path('readers/logout/', ReaderLogoutView.as_view(), name='reader-logout')
]