from django.urls import path
from .views import ProdutoView, ProdutoAddView, ProdutoEditRemov, ProdutoUpDateView, ProdutoDeleteView

urlpatterns = [
    path('produto', ProdutoView.as_view(), name='produtos'),
    path('produto/adicionar/', ProdutoAddView.as_view(), name='produto_adicionar'),
    path('editremov', ProdutoEditRemov.as_view(), name='editremov'),
    path('<int:pk>/produto/editar/', ProdutoUpDateView.as_view(), name='produto_editar'),
    path('<int:pk>/produto/apagar/', ProdutoDeleteView.as_view(), name='produto_apagar'),
]
