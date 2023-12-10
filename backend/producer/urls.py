from django.urls import path
from .views import ProducerListCreateView, ProducerRetrieveUpdateDestroyView, producer_login



# URLS que serão chamas no arquivo urls.py da pasta principal do projeto
urlpatterns = [
    path('producers/', ProducerListCreateView.as_view(), name='producer-list-create'),
    path('producers/<uuid:pk>/', ProducerRetrieveUpdateDestroyView.as_view(), name='producer-retrieve-update-destroy'),
    path('accounts/producer/login/', producer_login, name='producer-login'),
]