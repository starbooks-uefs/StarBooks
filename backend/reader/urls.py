from django.urls import path
from .views import SignUpView, ReaderLoginView, ReaderLogoutView, index

# URLS que serão chamas no arquivo urls.py da pasta principal do projeto
urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', ReaderLoginView.as_view(), name='login'),
    path('logout/', ReaderLogoutView.as_view(), name='logout'),
    path('home/', index, name='home'),
]