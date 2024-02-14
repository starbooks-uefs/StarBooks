from django.urls import path

from .views import get_purchase_by_id, get_bestseller

urlpatterns = [
  path('purchase/<int:id_book>/', get_purchase_by_id, name='purchase_detail'),
  path('bestseller/', get_bestseller, name='bestseller'),
]