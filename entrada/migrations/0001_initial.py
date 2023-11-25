# Generated by Django 4.2.7 on 2023-11-24 19:16

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('produto', '0002_produto_unidade'),
    ]

    operations = [
        migrations.CreateModel(
            name='EntradaProduto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Quantidade')),
                ('data_entrada', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data de Entrada')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entradas', to='produto.produto')),
            ],
            options={
                'verbose_name': 'Entrada de Produto',
                'verbose_name_plural': 'Entradas de Produtos',
                'ordering': ['-data_entrada'],
            },
        ),
    ]
