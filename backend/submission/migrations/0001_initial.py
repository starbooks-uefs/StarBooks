# Generated by Django 5.0.2 on 2024-02-16 22:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('adm', '0001_initial'),
        ('book', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_admin', models.ForeignKey(db_column='id_admin', on_delete=django.db.models.deletion.DO_NOTHING, to='adm.admin')),
                ('id_book', models.ForeignKey(db_column='id_book', on_delete=django.db.models.deletion.DO_NOTHING, to='book.book')),
            ],
            options={
                'db_table': 'submission',
                'unique_together': {('id_admin', 'id_book')},
            },
        ),
    ]
