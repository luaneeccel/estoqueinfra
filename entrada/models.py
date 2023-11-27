from django.db import models
from django.utils import timezone
from produto.models import Produto
from django.core.exceptions import ValidationError

class EntradaProduto(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name='entrada', verbose_name='Produto')
    quantidade = models.IntegerField('Quantidade')
    data_entrada = models.DateTimeField('Data de Entrada', default=timezone.now)

    class Meta:
        verbose_name = 'Entrada de Produto'
        verbose_name_plural = 'Entradas de Produtos'
        ordering = ['-data_entrada']

    def __str__(self):
        return f'{self.produto.nome} - {self.quantidade} unidades em {self.data_entrada}'

    def save(self, *args, **kwargs):
        self.clean()  # Chama o método clean manualmente
        super().save(*args, **kwargs)
