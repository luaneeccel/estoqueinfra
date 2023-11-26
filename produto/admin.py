from django.contrib import admin
from .models import Produto
from django.utils.html import format_html
# Register your models here.
@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    fields = ('nome', 'codigo', 'observacao', 'tipo', 'quantidade', 'quantidademin', 'unidade', 'foto', 'fotografia')
    list_display = ('nome', 'codigo', 'observacao', 'tipo', 'quantidade','quantidademin','foto', 'unidade', 'fotografia')
    readonly_fields = ['fotografia']


    def fotografia(self, obj):
        if obj.foto:
            return format_html('<img width="75px" src="{}" />', obj.foto.url)
        pass
