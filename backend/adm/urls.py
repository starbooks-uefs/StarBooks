from django.urls import path
from .views import AdminListCreateView, AdminRetrieveUpdateDestroyView, AdminLoginView, AdminLogoutView



# URLS que serão chamas no arquivo urls.py da pasta principal do projeto
urlpatterns = [
    path('admins/', AdminListCreateView.as_view(), name='admin-list-create'),
    path('admins/<uuid:pk>/', AdminRetrieveUpdateDestroyView.as_view(), name='admin-retrieve-update-destroy'),
    path('admins/login/', AdminLoginView.as_view(), name='admin-login'),
    path('admins/logout/', AdminLogoutView.as_view(), name='admin-logout'),
]