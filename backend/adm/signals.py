from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.db import transaction
from adm.models import Admin
from account.models import Account
from django.db.utils import IntegrityError

@receiver(post_migrate)
def create_root_admin(sender, **kwargs):
    try:
        if sender.name == 'adm':
            with transaction.atomic():
                admin = Admin.objects.create_admin(
                    username='root_admin',
                    email='admin@admin.com',
                    password= 'admin',  # Substitua pela senha desejada
                    user_type= 'Admin',
                    first_name= 'Root',
                    last_name= 'Admin',
                    birthdate= '1980-01-01',  # Substitua pela data de nascimento desejada
                    phone_number= '111-222-3333',  # Substitua pelo número de telefone desejado
                )
                print('Root admin created successfully.')
    
    except IntegrityError as e:
        print('Warning: Root admin already exists.')  
    except Exception as e:
        print(f"Erro no adm/signals.py: {e}")


'''@receiver(post_migrate)
def create_root_admin(sender, **kwargs):
    try:
        if sender.name == 'adm':
            with transaction.atomic():
                admin, created = Admin.objects.get_or_create(
                    username='root_admin',
                    defaults={
                        'email': 'admin@admin.com',  # Substitua pelo e-mail desejado
                        'password': 'admin',  # Substitua pela senha desejada
                        'user_type': 'Admin',
                        'first_name': 'Root',
                        'last_name': 'Admin',
                        'birthdate': '1980-01-01',  # Substitua pela data de nascimento desejada
                        'phone_number': '111-222-3333',  # Substitua pelo número de telefone desejado
                    }
                )
                if created:
                    print('Root admin created successfully.')
                else:
                    print('Root admin already exists.')
    
    except IntegrityError as e:
        print('Warning: Root admin already exists.')  
    except Exception as e:
        print(f"Erro no adm/signals.py: {e}")'''