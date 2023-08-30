# Generated by Django 3.2.11 on 2023-08-25 07:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(blank=True, max_length=4, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.product'),
        ),
    ]
