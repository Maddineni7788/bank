# Generated by Django 4.2.7 on 2024-01-04 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankingapp', '0005_deposit_email_transaction_email_withdrawal_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.CharField(max_length=15)),
                ('address', models.TextField(max_length=255)),
                ('account_type', models.CharField(choices=[('savings', 'Savings'), ('checking', 'Checking')], max_length=20)),
                ('initial_deposit', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
