# Generated by Django 5.0.2 on 2024-02-17 02:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_initial'),
        ('purchase', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='id_book',
            field=models.ForeignKey(db_column='id_book', on_delete=django.db.models.deletion.CASCADE, to='book.book'),
        ),
    ]
