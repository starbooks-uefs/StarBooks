from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Reader

@receiver(post_migrate)
def create_root_reader_users(sender, **kwargs):
    Reader.objects.get_or_create(
        username='root_reader',
        defaults={
            'email': 'reader@reader.com',
            'password': 'reader',
            'is_staff': False,
            'is_superuser': False,
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