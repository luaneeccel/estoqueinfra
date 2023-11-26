from django.shortcuts import render, redirect
from .forms import SaidaProdutoForm
#from .models import Produto


def saida_produto(request):
    if request.method == 'POST':
        form = SaidaProdutoForm(request.POST)
        if form.is_valid():
            Saida = form.save()

            # Atualizar a quantidade do produto com base na entrada
            produto = saida.produto
            produto.quantidade =produto.quantidade - saida.quantidade
            produto.save()

            return redirect('lista_produtos')  # Redirecionar para a lista de produtos
    else:
        form = SaidaProdutoForm()

    return render(request, 'saida_produto.html', {'form': form})
