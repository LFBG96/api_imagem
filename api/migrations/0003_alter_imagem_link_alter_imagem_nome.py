# Generated by Django 4.2.7 on 2023-11-12 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_imagem_link_alter_imagem_nome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagem',
            name='link',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='imagem',
            name='nome',
            field=models.CharField(max_length=200),
        ),
    ]
