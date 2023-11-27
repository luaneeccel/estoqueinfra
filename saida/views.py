from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView
from django.contrib import messages
from .forms import SaidaProdutoForm
from .models import SaidaProduto, Produto
from django.http import JsonResponse
from django.shortcuts import get_object_or_404


class SaidaProdutoView(View):
    template_name = 'saida_produto.html'

    def get(self, request):
        form = SaidaProdutoForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = SaidaProdutoForm(request.POST)
        if form.is_valid():
            saida = form.save()

            # Atualizar a quantidade do produto com base na saída
            produto = saida.produto
            produto.quantidade -= saida.quantidade
            produto.save()

            # Adicione uma mensagem de sucesso
            messages.success(request, 'Saída concluída com sucesso!')

            # Redirecione para alguma página ou URL
            return redirect('saida_produto_list')  # Substitua 'saida_produto_list' pela sua URL desejada

        # Se o formulário não for válido, continue renderizando a página com o formulário
        return render(request, self.template_name, {'form': form})


def obter_nome_produto(request):
    codigo = request.GET.get('codigo', '')
    produto = get_object_or_404(Produto, codigo=codigo)

    data = {'nome_produto': produto.nome}
    return JsonResponse(data)


class SaidaProdutoListView(ListView):
    model = SaidaProduto
    template_name = 'saida_produto_list.html'
    context_object_name = 'saidas'
