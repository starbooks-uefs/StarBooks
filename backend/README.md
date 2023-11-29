# Instruções
Primeiro entre na pasta back end (a mais externa)
## Instalando dependências
- Criar venv (virtual enviroment)
```console
pip install virtualenv
python -m venv venv
```
### Ativar venv

Linux:
```console
source venv/bin/activate
```
Windows:
```console
venv/Scripts/activate
```

### Instalar dependências
```console
pip install -r requirements.txt
```
## Para testar banco de dados
Entrar com o comando:
```console
python manage.py dbshell
```
Vai aparecer 'postgres=>'
- Para listar todos as tabelas do bd atual
```console
\dt
```
- Exibir a estrutura de uma tabela específica (substitua nome_da_tabela pelo nome real da tabela):
```console
\d nome_da_tabela
```
Para sair apertar ctrl+d

## Para executar
Entrar com o comando:
```console
python manage.py runserver
```
### Rotas

As rotas ainda não estão autenticando, provavelmente porque não fiz as migrações.
Além disso, precisa-se rever como funciona a linha 134 no arquivo settings.py, que aparentemente precisaremos usar:
```console
AUTH_USER_MODEL = 
```
- Login
```console
http://127.0.0.1:8000/reader/login/
```
- Cadastro
```console
http://127.0.0.1:8000/reader/signup/
```
