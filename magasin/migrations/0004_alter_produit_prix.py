# Generated by Django 5.0.2 on 2024-04-22 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magasin', '0003_rename_type_prod_produit_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='prix',
            field=models.FloatField(),
        ),
    ]