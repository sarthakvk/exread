# Generated by Django 3.1.1 on 2020-11-01 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='invoice',
            old_name='invoice_numbsers',
            new_name='invoice_numbers',
        ),
    ]