# Generated by Django 5.2 on 2025-04-13 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formularios', '0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuarios',
            name='senhas',
            field=models.TextField(default='senhas'),
        ),
    ]
