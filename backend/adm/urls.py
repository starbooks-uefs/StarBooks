from django.urls import path
from .views import AdminListCreateView, AdminRetrieveUpdateDestroyView, admin_login



# URLS que serão chamas no arquivo urls.py da pasta principal do projeto
urlpatterns = [
    path('admins/', AdminListCreateView.as_view(), name='Admin-list-create'),
    path('admins/<uuid:pk>/', AdminRetrieveUpdateDestroyView.as_view(), name='Admin-retrieve-update-destroy'),
    path('accounts/admin/login/', admin_login, name='admin-login'),
]