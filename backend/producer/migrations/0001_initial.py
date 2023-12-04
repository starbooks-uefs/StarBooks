# Generated by Django 5.0 on 2023-12-04 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producer',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('password', models.CharField(max_length=16)),
                ('email', models.CharField(max_length=60, unique=True)),
                ('birthdate', models.DateTimeField()),
                ('phone_number', models.IntegerField(blank=True, null=True)),
                ('cnpj', models.IntegerField(unique=True)),
                ('bank_name', models.CharField(max_length=25)),
                ('bank_agency', models.IntegerField()),
                ('number_account', models.IntegerField()),
                ('account_type', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'producer',
                'managed': False,
            },
        ),
    ]
