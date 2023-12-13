# Instruções
Primeiro, estar no diretório /StarBooks
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

```console
cd backend/
```
### Instalar dependências
```console
pip install -r requirements.txt
```
# QUAISQUER COMANDOS COM manage.py PRECISAM ESTAR NO DIRETÓRIO: StarBooks/backend
```console
cd backend/
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
OBS: Para sair, apertar ctrl+d

## Para executar
Entrar com o comando:
```console
python manage.py runserver
```
### Rotas

#### Teste para listar e criar usuários
- Listar (GET)
```console
http://127.0.0.1:8000/api/readers/
```
- Criar (POST)
```console
http://127.0.0.1:8000/api/readers/
```
Exemplo de POST:

```console
{
  "id": "123e4567-e89b-12d3-a456-426614174001",
  "name": "John",
  "last_name": "Doe",
  "password": "password123",
  "email": "john.doe@example.com",
  "birthdate": "2000-01-01T12:00:00Z",
  "phone_number": 1234567890,
  "cpf": 123456789,
  "gender": "Male",
  "cardholder": "John Doe",
  "cvv": 123,
  "card_number": 123456789,
  "card_date": "2023-12-01T00:00:00Z"
}
```

#### Teste para listar, atualizar e deletar usuário pelo UUID:

- Listar (GET)
```console
http://127.0.0.1:8000/api/readers/<uuid:pk>/
```
- Atualizar (PUT)
```console
http://127.0.0.1:8000/api/readers/<uuid:pk>/
```
- Deletar (DELETE)
```console
http://127.0.0.1:8000/api/readers/<uuid:pk>/
```



