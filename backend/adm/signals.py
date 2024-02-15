from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Admin

@receiver(post_migrate)
def create_root_admin(sender, **kwargs):
    Admin.objects.get_or_create(
        username='root_admin',
        defaults={
            'email': 'admin@admin.com',  # Substitua pelo e-mail desejado
            'password': 'admin',  # Substitua pela senha desejada
            'is_staff': True,
            'is_superuser': True,
            'first_name': 'Root',
            'last_name': 'Admin',
            'birthdate': '1980-01-01',  # Substitua pela data de nascimento desejada
            'phone_number': '111-222-3333',  # Substitua pelo número de telefone desejado
        }
    )

from producer.models import Producer

@receiver(post_migrate)
def create_root_producer(sender, **kwargs):
    Producer.objects.get_or_create(
        username='root_producer',
        defaults={
            'email': 'producer@producer.com',
            'password': 'producer',
            'is_staff': False,
            'is_superuser': False,
            'cnpj': 12345678901234,
            'bank_name': 'Banco ABC',
            'bank_agency': 9876,
            'number_account': 12345678,
            'account_type': 'Corrente',
            'first_name': 'Root',
            'last_name': 'Producer',
            'birthdate': '1985-05-15',
            'phone_number': '987-654-3210',
        }
    )
    
from reader.models import Reader

@receiver(post_migrate)
def create_root_reader(sender, **kwargs):
    Reader.objects.get_or_create(
        username='root_reader',
        defaults={
            'email': 'reader@reader.com',
            'password': 'reader',
            'is_staff': False,
            'is_superuser': False,
            'cpf': 12345678901,
            'gender': 'Male',
            'cardholder': 'John Doe',
            'cvv': 123,
            'card_number': '1234567890123456',
            'card_date': '2023-12-31',
            'first_name': 'Root',
            'last_name': 'Reader',
            'birthdate': '1990-01-01',
            'phone_number': '123-456-7890',
        }
    )
    
'''from book.models import Book

@receiver(post_migrate)
def create_first_book(sender, **kwargs):
    Book.objects.get_or_create(
        defaults={
            "id":"1", 
            "name": "Meu Livro",
            "date": "2023-12-31",
            "submission_reason": "hddcd",
            "gender": "Ficção",
            "publisher": "Minha Editora",
            "edition": 1,
            "synopsis": "Uma breve sinopse do livro.",
            "pdf_url": "http://exemplo.com/livro.pdf",
            "price": 29.99,
            "pages_number": 200,
            "cover_url": "http://exemplo.com/capa.jpg",
            "language": "Português",
            "submission_status": True,
            "submission_date": "2023-12-31",
            "producer_id": 2
        }
    )'''