# Generated by Django 5.2 on 2025-04-13 23:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formularios', '0006_alter_usuarios_senhas'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuarios',
            old_name='emails',
            new_name='bandas',
        ),
        migrations.RenameField(
            model_name='usuarios',
            old_name='senhas',
            new_name='filmes',
        ),
    ]
