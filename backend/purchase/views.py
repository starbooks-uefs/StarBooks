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
    bestseller = Book.objects.annotate(purchase_count=Count('purchases')).order_by('-purchase_count')[0]
    purchase_count = bestseller.purchase_count
  except Book.DoesNotExist:
    purchase_count = 0

  # Busca o preço do ebook
  price = bestseller.price

  # Calcula o valor total arrecadado
  total_revenue = purchase_count * price

  # Retorna um dicionário em formato JSON
  return JsonResponse({'id_book': bestseller.id, 'name': bestseller.name, 'purchase_count': purchase_count, 'total_revenue': total_revenue})