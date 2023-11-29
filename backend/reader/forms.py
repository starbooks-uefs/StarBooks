from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Reader

# Aqui ficam os modelos de formulário, quais campos quer que apareça
class ReaderSignUpForm(UserCreationForm):
    class Meta:
        model = Reader
        fields = ('name', 'last_name', 'email', 'password', 'birthdate', 'phone_number', 'cpf', 'gender', 'cardholder', 'cvv', 'card_number', 'card_date')

class ReaderLoginForm(AuthenticationForm):
    class Meta:
        model = Reader
        fields = ('email', 'password')