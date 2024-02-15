from django.urls import path
from .views import ChangePasswordView


# URLS que serão chamas no arquivo urls.py da pasta principal do projeto
urlpatterns = [
    path('users/<int:pk>/change_password/', ChangePasswordView.as_view(), name='change-password'),
   
]