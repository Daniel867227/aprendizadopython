# Generated by Django 5.2 on 2025-04-13 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formularios', '0004_usuarios_senhas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='senhas',
            field=models.CharField(default='senhas', max_length=50),
        ),
    ]
