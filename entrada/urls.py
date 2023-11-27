# entrada/urls.py
from django.urls import path
from .views import EntradaProdutoView, EntradaProdutoListView

urlpatterns = [
    path('entrada_produto/', EntradaProdutoView.as_view(), name='entrada_produto'),
    path('entrada_produto_list/', EntradaProdutoListView.as_view(), name='entrada_produto_list'),

]
