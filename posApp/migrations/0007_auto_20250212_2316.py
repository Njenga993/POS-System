# Generated by Django 3.2.3 on 2025-02-12 20:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posApp', '0006_inventory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='stock',
        ),
        migrations.DeleteModel(
            name='Inventory',
        ),
    ]
