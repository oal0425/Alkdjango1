# Generated by Django 4.2.1 on 2023-05-25 02:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('StockControl', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='name',
            new_name='nombre',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='price',
            new_name='precio',
        ),
    ]
