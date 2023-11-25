# Generated by Django 4.2.7 on 2023-11-24 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0002_produto_unidade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='quantidade',
            field=models.DecimalField(decimal_places=0, help_text='Quantidade em Estoque do produto', max_digits=5, max_length=5, verbose_name='Quantidade'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='quantidademin',
            field=models.DecimalField(decimal_places=0, max_digits=5, max_length=5, verbose_name='Quantidade minima'),
        ),
    ]
