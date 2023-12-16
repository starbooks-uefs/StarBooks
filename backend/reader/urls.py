from django.urls import path
from .views import (
    ReaderListCreateView, 
    ReaderRetrieveUpdateDestroyView, 
    ReaderLoginView, ReaderLogoutView, 
    ReaderAddPurchaseToLibraryView,  
    ReaderPurchasesView,
    ReaderPurchaseDetailView)

# URLS que serão chamas no arquivo urls.py da pasta principal do projeto
urlpatterns = [
    path('readers/', ReaderListCreateView.as_view(), name='reader-list-create'),
    path('readers/<int:id_reader>/', ReaderRetrieveUpdateDestroyView.as_view(), name='reader-retrieve-update-destroy'),
    path('readers/login/', ReaderLoginView.as_view(), name='reader-login'),
    path('readers/logout/', ReaderLogoutView.as_view(), name='reader-logout'),
    
    path('readers/add_purchase_to_library/', ReaderAddPurchaseToLibraryView.as_view(), name='reader-add-purchase-to-library'),
    path('readers/<int:id_reader>/purchases/', ReaderPurchasesView.as_view(), name='reader-purchases'),
    path('readers/<int:id_reader>/purchases/<int:id_purchase>/', ReaderPurchaseDetailView.as_view(), name='reader-purchase-detail')
]