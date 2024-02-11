from django.urls import path
from .views import CartAPIView

urlpatterns = [
    path('cart/', CartAPIView.as_view(), name='cart_api'),
]