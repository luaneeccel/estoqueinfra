from django.db import models
from django.utils import timezone
# from produto.models import  Produto

class EntradaProduto(models.Model):
    produto = models.ForeignKey('produto.Produto' , on_delete=models.CASCADE, related_name='produto', verbose_name='Produto')
    quantidade = models.IntegerField('Quantidade')
    data_entrada = models.DateTimeField('Data de Entrada', default=timezone.now)

    class Meta:
        verbose_name = 'Entrada de Produto'
        verbose_name_plural = 'Entradas de Produtos'
        ordering = ['-data_entrada']

    def __str__(self):
        return f'{self.produto.nome} - {self.quantidade} unidades em {self.data_entrada}'