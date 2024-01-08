# Generated by Django 4.2.7 on 2024-01-04 13:02

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('bankingapp', '0006_account'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='account_number',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
