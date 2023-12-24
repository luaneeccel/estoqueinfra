# Generated by Django 4.2.7 on 2023-12-19 11:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0005_alter_produto_codigo'),
        ('entrada', '0003_alter_entradaproduto_quantidade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entradaproduto',
            name='produto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entrada', to='produto.produto', verbose_name='Produto'),
        ),
    ]
