from django.db.models import F, Count
from django.http import JsonResponse
from .models import Purchase, Book

def get_purchase_by_id(request, id_book):
  """
  Função para obter a quantidade de vezes que um ebook foi comprado e o valor total arrecadado, retornando um JSON.

  Args:
    request: requisição HTTP
    id_book: ID do ebook

  Returns:
    Dicionário em formato JSON com a quantidade de compras, valor total arrecadado e preço do ebook
  """

  # Busca a quantidade de compras do ebook
  try:
    purchase_count = Purchase.objects.filter(id_book=id_book).count()
  except Purchase.DoesNotExist:
    purchase_count = 0

  # Busca o preço do ebook
  try:
    book = Book.objects.get(pk=id_book)
    price = book.price
  except Book.DoesNotExist:
    price = 0

  # Calcula o valor total arrecadado
  total_revenue = purchase_count * price

  # Retorna um dicionário em formato JSON
  return JsonResponse({'purchase_count': purchase_count, 'total_revenue': total_revenue, 'price': price})


def get_bestseller(request):
  """
  Função para obter o livro mais vendido e o valor total arrecadado, retornando um JSON.

  Args:
    request: requisição HTTP

  Returns:
    Dicionário em formato JSON com o ID do livro, nome, quantidade de compras e valor total arrecadado
  """

  # Busca o livro mais vendido
  try:
    bestseller = Book.objects.annotate(purchase_count=Count('purchase')).order_by('-purchase_count')[0]
    purchase_count = bestseller.purchase_count
  except Book.DoesNotExist:
    purchase_count = 0

  # Busca o preço do ebook
  price = bestseller.price

  # Calcula o valor total arrecadado
  total_revenue = purchase_count * price

  # Retorna um dicionário em formato JSON
  return JsonResponse({'id_book': bestseller.id, 'name': bestseller.name, 'purchase_count': purchase_count, 'total_revenue': total_revenue})


def get_bestseller_by_author_by_producer(author_name, producer_id):
  """
  Função que retorna o livro mais vendido de um autor específico para um produtor específico em formato JSON.

  Args:
    author_name: Nome do autor.
    producer_id: ID do produtor.

  Returns:
    Dicionário JSON com informações do livro mais vendido.
  """

  # Filtra os livros pelo autor e produtor
  books = Book.objects.filter(
    author=author_name,
    id_producer=producer_id,
  )

  # Cálculo manual da soma das compras para cada livro
  for book in books:
    book.total_sales = sum(purchase.quantity for purchase in book.purchase_set.filter(status='approved'))

  # Ordena os livros pela soma das compras
  bestseller = books.order_by('-total_sales').first()

  if bestseller:
    # Prepara dados para JSON
    return JsonResponse({
      "id": bestseller.id,
      "name": bestseller.name,
      "author": bestseller.author,
      "total_sales": bestseller.total_sales,
    })
  else:
    return JsonResponse({"message": "Nenhum livro encontrado."})