from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Producer

@receiver(post_migrate)
def create_root_producer(sender, **kwargs):
    Producer.objects.get_or_create(
        username='root_producer',
        defaults={
            'email': 'producer@producer.com',
            'password': 'producer',
            'is_staff': False,
            'is_superuser': False,
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