# /urls.py
from django.urls import path
from .views import SaidaProdutoView, SaidaProdutoListView

urlpatterns = [
    path('saida_produto/', SaidaProdutoView.as_view(), name='saida_produto'),
    path('saida_produto_list/', SaidaProdutoListView.as_view(), name='saida_produto_list'),

    # Adicione a URL para listar as entradas aqui
    # path('entrada/lista/', SuaViewDeListagem.as_view(), name='entrada_produto_list'),
]
