from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Admin

@receiver(post_migrate)
def create_root_admin_users(sender, **kwargs):
    Admin.objects.get_or_create(
        username='root_admin',
        defaults={
            'email': 'admin@admin.com',  # Substitua pelo e-mail desejado
            'password': 'admin',  # Substitua pela senha desejada
            'is_staff': True,
            'is_superuser': True,
            'user_type': 'Admin',
            'first_name': 'Root',
            'last_name': 'Admin',
            'birthdate': '1980-01-01',  # Substitua pela data de nascimento desejada
            'phone_number': '111-222-3333',  # Substitua pelo número de telefone desejado
        }
    )
