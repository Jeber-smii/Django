# Generated by Django 5.0.2 on 2024-05-11 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magasin', '0006_commande_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='commande',
            name='qte',
            field=models.IntegerField(default=1),
        ),
    ]
