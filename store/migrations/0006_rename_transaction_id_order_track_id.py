# Generated by Django 3.2.11 on 2023-08-25 10:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20230825_1316'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='transaction_id',
            new_name='track_id',
        ),
    ]
