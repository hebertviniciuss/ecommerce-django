# Generated by Django 4.2.3 on 2023-07-25 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0002_alter_categoria_nome_alter_marca_nome_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='imagem_produto',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Imagem do Produto'),
        ),
    ]
