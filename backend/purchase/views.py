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
