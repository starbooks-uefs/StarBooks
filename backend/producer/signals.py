from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.db import transaction
from producer.models import Producer
from book.models import Book, SubmissionStatus
from django.db.utils import IntegrityError

@receiver(post_migrate)
def create_root_producer(sender, **kwargs):
    try:
        if sender.name == 'producer':
            with transaction.atomic():
                producer, created = Producer.objects.get_or_create(
                    username='root_producer',
                    defaults={
                        'email': 'producer@producer.com',
                        'password': 'producer',
                        'user_type': 'Producer',
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
                if created:
                    print('Root producer created successfully.')
                else:
                    print('Root producer already exists.')
    except IntegrityError as e:
        print('Warning: Root producer already exists.')
    except Exception as e:
        print(f"Erro no producer/signals.py: {e}")
                    
'''@receiver(post_migrate, sender=apps.get_app_config('producer'))
def create_default_book(sender, **kwargs):
    try:
        with transaction.atomic():
            # Obtém o produtor padrão (root_producer)
            default_producer = Producer.objects.get(username='root_producer')

            # Cria o livro padrão associado ao produtor padrão
            default_book = Book.objects.create(
                name='Default Book',
                author='Default Author',
                gender='Default Gender',
                publisher='Default Publisher',
                id_producer=default_producer,
                edition=1,
                synopsis='Default Synopsis',
                pdf_url='https://example.com/default_book.pdf',
                price=10.0,
                pages_number=100,
                date='2023-01-01',
                cover_url='https://example.com/default_cover.jpg',
                rating=5,
                language='English',
                submission_status=SubmissionStatus.approved,
                submission_date='2023-01-01',
                submission_reason='Default Book',
            )
            print('Default Book created successfully!')
    except IntegrityError:
        print('Root producer does not exist yet. Skipping book creation.')'''