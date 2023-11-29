from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from .models import Reader
from .forms import ReaderSignUpForm, ReaderLoginForm
from django.shortcuts import render, redirect
from django.contrib.auth import login

# GET - O que aparece quando acessa a url
# POST - Lógica para o que acontece quando realiza login/cadastro
class SignUpView(CreateView):
    # caminho do template na pasta "templates"
    template_name = 'signup.html'
    
    def get(self, request, *args, **kwargs):
        # Modelo do form
        form = ReaderSignUpForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        # Modelo do form
        form = ReaderSignUpForm(request.POST)
        #return redirect('home')
        # Verifica se os dados são válidos
        if form.is_valid():
            # salva no bd
            user = form.save()
            # tenta logar
            login(request, user)
            # vai pra home
            # Detalhe: o redirect chama o NOME da página, e não o endpoint
            return redirect('home')
        return render(request, self.template_name, {'form': form})

class ReaderLoginView(LoginView):
    # caminho do template na pasta "templates"
    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        form = ReaderLoginForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = ReaderLoginForm(data=request.POST)
        #return redirect('home')
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        return render(request, self.template_name, {'form': form})

class ReaderLogoutView(LogoutView):
    
    pass

# pagina inicial
def index(request):
    return render(request, 'index.html')