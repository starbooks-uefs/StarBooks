# Generated by Django 5.0.2 on 2024-02-15 02:39

import django.contrib.auth.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reader',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('cpf', models.CharField(max_length=11, unique=True)),
                ('gender', models.CharField(blank=True, max_length=15, null=True)),
                ('cardholder', models.CharField(max_length=50)),
                ('cvv', models.IntegerField()),
                ('card_number', models.CharField(max_length=20)),
                ('card_date', models.DateField()),
            ],
            options={
                'db_table': 'reader',
            },
            bases=('user.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]