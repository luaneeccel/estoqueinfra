from django.contrib import admin
from .models import SaidaProduto

@admin.register(SaidaProduto)
class SaidaProdutoAdmin(admin.ModelAdmin):
    list_display = ['produto', 'quantidade', 'data_saida']
    search_fields = ('produto.name', )  # Permite pesquisar por nome ou código do produto
    list_filter = ('data_saida',)
    # date_hierarchy = 'data_entrada'  # Adiciona navegação por data
    ordering = ('-data_saida',)  # Exibe as entradas mais recentes primeiro
    fields = ('produto', 'quantidade', 'data_saida')  # Campos editáveis na página de adição

    def save_model(self, request, obj, form, change):
        """
        Sobrescreve o método save_model para atualizar a quantidade do produto
        quando uma entrada de produto é salva.
        """
        obj.save()
        produto = obj.produto
        produto.quantidade -= obj.quantidade
        produto.save()