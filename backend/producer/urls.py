from django.urls import path
from .views import ProducerListCreateView, ProducerRetrieveUpdateDestroyView, ProducerLoginView, ProducerLogoutView, UpdateProducerView



# URLS que serão chamas no arquivo urls.py da pasta principal do projeto
urlpatterns = [
    path('producers/', ProducerListCreateView.as_view(), name='producer-list-create'),
    path('producers/<int:pk>/', ProducerRetrieveUpdateDestroyView.as_view(), name='producer-retrieve-update-destroy'),
    path('producers/login/', ProducerLoginView.as_view(), name='producer-login'),
    path('producers/logout/', ProducerLogoutView.as_view(), name='producer-logout'),
    path('producers/update/<int:pk>/', UpdateProducerView.as_view(), name='update-producer'),
]

