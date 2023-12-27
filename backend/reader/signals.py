from django.db.models.signals import post_migrate
from django.dispatch import receiver
from reader.models import Reader
from django.db import transaction
from django.db.utils import IntegrityError

@receiver(post_migrate)
def create_root_reader(sender, **kwargs):
    try:
        if sender.name == 'reader':
            with transaction.atomic():
                reader, created = Reader.objects.get_or_create(
                    username='root_reader',
                    defaults={
                        'email': 'reader@reader.com',
                        'password': 'reader',
                        'user_type': 'Reader',
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
                if created:
                    print('Root reader created successfully.')
                else:
                    print('Root reader already exists.')
    
    except IntegrityError as e:
        print('Warning: Root producer already exists.')            
    except Exception as e:
        print(f"Erro no reader/signals.py: {e}")
