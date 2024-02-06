# StarBooks
Sistema de uma editora virtual
# StarBooks
Sistema de uma editora virtual

# Instruções
- Entrar no diretório do projeto
```console
cd backend/
```
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
OBS: Para sair, apertar ctrl+d

## Para executar
Entrar com o comando:
```console
python manage.py runserver
```