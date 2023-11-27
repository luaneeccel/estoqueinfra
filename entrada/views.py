from django.shortcuts import render, redirect
from django.views import View
from .forms import EntradaProdutoForm
from django.views.generic import ListView
from .models import EntradaProduto
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView
from django.contrib import messages
from .forms import EntradaProdutoForm
from .models import EntradaProduto, Produto
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from produto.models import Produto  # Certifique-se de importar corretamente o modelo Produto

from django.db.models import F


class EntradaProdutoView(View):
    template_name = 'entrada_produto.html'

    def get(self, request):
        form = EntradaProdutoForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = EntradaProdutoForm(request.POST)
        if form.is_valid():
            entrada = form.save()

            # Atualizar a quantidade do produto com base na entrada
            produto = entrada.produto
            produto.quantidade += entrada.quantidade
            produto.save()

            # Adicione uma mensagem de sucesso
            messages.success(request, 'Entrada concluída com sucesso!')

            return redirect('entrada_produto_list')  # Redirecionar para a lista de produtos

        return render(request, self.template_name, {'form': form})


def obter_nome_produto(request):
    codigo = request.GET.get('codigo', '')
    produto = get_object_or_404(Produto, codigo=codigo)

    data = {'nome_produto': produto.nome}
    return JsonResponse(data)




class EntradaProdutoListView(ListView):
    model = EntradaProduto
    template_name = 'entrada_produto_list.html'
    context_object_name = 'entradas'

    ## copiar para todas funções e Subustituir o EntradaProdutoListView pelo nome das classes
    ##dar import
    # from django.db.models import F

    def get_context_data(self, **kwargs):
        context = super(EntradaProdutoListView, self).get_context_data(**kwargs)
        context['qtd_produtos'] = Produto.objects.count()
        context['min_produtos'] = Produto.objects.filter(quantidade__lt=F('quantidademin'), quantidade__gt=0).count()
        context['zero_produtos'] = Produto.objects.filter(quantidade=0).count()
        return context
