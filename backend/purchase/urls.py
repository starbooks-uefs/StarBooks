from django.urls import path

from .views import get_bestseller_by_author_by_producer, get_purchase_by_id, get_bestseller

urlpatterns = [
  path('purchase/<int:id_book>/', get_purchase_by_id, name='purchase_detail'),
  path('bestseller/', get_bestseller, name='bestseller'),
  path('bestseller/author/<str:author_name>/producer/<int:producer_id>/', get_bestseller_by_author_by_producer, name='bestseller-by-author'),
]