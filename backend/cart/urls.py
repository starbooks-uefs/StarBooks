from django.urls import path
from .views import CreateCartView, ClearCartView, RetrieveCartView, AddToCartView 

urlpatterns = [
    path('cart/create/', CreateCartView.as_view(), name='create_cart'),
    path('cart/clear/', ClearCartView.as_view(), name='clear_cart'),
    path('cart/retrieve/', RetrieveCartView.as_view(), name='retrieve_cart'),
    path('cart/addToCart/', AddToCartView.as_view(), name='add_to_cart'),
]