from django.contrib import admin
from .models import Produto
# Register your models here.
@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'codigo', 'observacao', 'tipo', 'quantidade','quantidademin','foto', 'unidade')