# Generated by Django 4.2.7 on 2023-11-12 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_imagem_link_alter_imagem_nome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagem',
            name='link',
            field=models.URLField(unique=True),
        ),
    ]
