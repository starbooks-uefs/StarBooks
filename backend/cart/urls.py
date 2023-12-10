from django.urls import path
from .views import GetCartView, CreateCartView, UpdateCartView

urlpatterns = [
    path('cart/obterPorLeitor/', GetCartView.as_view(), name='get_cart'),
    path('cart/criar/<int:pk>/', CreateCartView.as_view(), name='create_cart'),
    path('cart/atualizarPorLeitor/<int:pk>/', UpdateCartView.as_view(), name='update_cart'),
]