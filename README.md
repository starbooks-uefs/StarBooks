# StarBooks
Sistema de uma editora virtual

Link do backend Hospedado: https://starbooks-backend-uw7b.onrender.com

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

# Rotas

## Reader

- Ver todos os leitores / Criar leitor
```console
/api/readers/
```

- Ver / Atualizar / Deletar leitor específico
```console
/api/readers/<int:pk>/
```

- Login / Logout
```console
/api/readers/login/
/api/readers/logout/
```

- Adicionar compra a biblioteca
```console
/api/readers/add_purchase_to_library/
```

- Ver todas as compras de um leitor
```console
/api/readers/<int:id_reader>/purchases/
```

- Ver compra específica de leitor 
```console
/api/readers/<int:id_reader>/purchases/<int:id_purchase>/
```

- Ver livros do leitor 
```console
/api/readers/<int:id_reader>/books/
```

## Producer

- Ver todos os produtores / Criar produtor
```console
/api/producers/
```

- Ver / Atualizar / Deletar leitor específico
```console
/api/producers/<int:pk>/
```

- Login / Logout
```console
/api/producers/login/
/api/producers/logout/
```

## Admin

- Ver todos os admins / Criar admin
```console
/api/admins/
```

- Ver / Atualizar / Deletar admin específico
```console
/api/admins/<int:pk>/
```

- Login / Logout
```console
/api/admins/login/
/api/admins/logout/
```

## Book
- Ver todos os livros / Criar livro
```console
/api/books/
```
- Listar livros por parametros / por nome, gênero, ano, editora, autor
```console
/api/books/search/?gender=name
/api/books/search/?year=name
/api/books/search/?name=name
/api/books/search/?author=name
/api/books/search/?publisher=name
```

- Ver / Atualizar (todos os campos) / Deletar livro específico
```console
/api/books/<int:pk>/
```

- Atualizar preço do livro (apenas o campo 'price')
```console
/api/update_book_price/<int:pk>/
```

- Resgatar livro pelo gênero
```console
/api/books/retrieve/gender/<str:gender>/
```

- Resgatar livro pelo autor
```console
/api/books/retrieve/author/<str:author>/
```

- Resgatar livros do mês atual
```console
/api/books/current-month/
```

## Cart

A lógica do carrinho é para usuários autenticados, então não precisa passar nenhum identificador pois a autenticação já atribui o id as views

- Criar carrinho
```console
/api/cart/create/
```

- Resgatar carrinho
```console
/api/cart/retrieve/  
```

- Adicionar livro ao carrinho
```console
/api/cart/add/<int:id_book>/
```

- Limpar carrinho
```console
/api/cart/clear/
```

- Remover livro do carrinho
```console
/api/cart/clear/<int:pk>/
```
