from django.shortcuts import render, redirect
from .forms import EntradaProdutoForm
#from .models import Produto


def entrada_produto(request):
    if request.method == 'POST':
        form = EntradaProdutoForm(request.POST)
        if form.is_valid():
            entrada = form.save()

            # Atualizar a quantidade do produto com base na entrada
            produto = entrada.produto
            produto.quantidade += entrada.quantidade
            produto.save()

            return redirect('lista_produtos')  # Redirecionar para a lista de produtos
    else:
        form = EntradaProdutoForm()

    return render(request, 'entrada_produto.html', {'form': form})
