from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .models import Purchase

def get_purchase_by_id(request, id_book):
  """
  Função para obter a quantidade de vezes que um ebook foi comprado.

  Args:
    request: requisição HTTP
    id_book: ID do ebook

  Returns:
    Dicionário com a quantidade de compras do ebook
  """

  # Busca a quantidade de compras do ebook
  try:
    purchase_count = Purchase.objects.filter(id_book=id_book).count()
  except Purchase.DoesNotExist:
    purchase_count = 0

  # Retorna a quantidade de compras
  return render(request, 'purchase_detail.html', {'purchase_count': purchase_count})

