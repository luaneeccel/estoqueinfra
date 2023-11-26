from django.db import models
from django.utils import timezone
from produto.models import  Produto
from django.core.exceptions import ValidationError
class SaidaProduto(models.Model):
    produto = models.ForeignKey('produto.Produto' , on_delete=models.CASCADE, related_name='saida', verbose_name='Produto')
    quantidade = models.IntegerField('Quantidade')
    data_saida = models.DateTimeField('Data de Saida', default=timezone.now)


    class Meta:
        verbose_name = 'Saida de Produto'
        verbose_name_plural = 'Saidas de Produtos'
        ordering = ['-data_saida']

    def __str__(self):
        return f'{self.produto.nome} - {self.quantidade} unidades em {self.data_saida}'

    def clean(self):
        if self.quantidade > self.produto.quantidade:
            raise ValidationError('Quantidade inserida é maior que em estoque.')

    def save(self, *args, **kwargs):
        self.clean()  # Chama o método clean manualmente
        super().save(*args, **kwargs)