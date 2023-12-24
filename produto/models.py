from django.db import models
from stdimage import StdImageField
# from django_select2 import forms as s2forms
# Create your models here.
class Produto(models.Model):
    nome=models.CharField('Nome', max_length=50, help_text='Nome do Produto')
    codigo = models.CharField('Código', max_length=10,unique=True, help_text='Código do Produto')
    observacao = models.CharField('Observações', max_length=200, help_text='Observações')
    tipo = models.CharField('Tipo', max_length=50, help_text='Tipo do Produto')
    unidade = models.CharField('Unidade', max_length=50, help_text='Unidade', default='')
    quantidade = models.IntegerField('Quantidade', help_text='Quantidade em Estoque do produto')
    quantidademin = models.IntegerField('Quantidade minima')
    foto = StdImageField('Foto', upload_to='produtos', variations={'thumbnail':{'width':100, 'height':100, 'crop':True}}, delete_orphans=True, null=True, blank=True)
    class Meta:
        verbose_name ='Produto'
        verbose_name_plural='Produtos'
        ordering = ['nome', ]

    def __str__(self):
        return self.nome
