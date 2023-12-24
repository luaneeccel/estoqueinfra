from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.db.models import Q

# Create your views here.
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import Produto
from .forms import ProdutoModelForm
class ProdutoView(ListView):
    model = Produto
    template_name = 'produto.html'

    def get_queryset(self, *args, **kwargs):
        buscar = self.request.GET.get('buscar')
        buscar_codigo = self.request.GET.get('buscar_codigo')

        qs = super(ProdutoView, self).get_queryset(*args, **kwargs)

        if buscar:
            qs = qs.filter(Q(nome__icontains=buscar) | Q(codigo__icontains=buscar_codigo))

        paginator = Paginator(qs, 2)
        listagem = paginator.get_page(self.request.GET.get('page'))
        return listagem
class ProdutoAddView(CreateView):
    form_class = ProdutoModelForm
    model = Produto
    template_name = 'produto_form.html'
    success_url = reverse_lazy('produtos')

    def form_valid(self, form):
        # Lógica padrão de validação do formulário
        response = super().form_valid(form)

        # Se o botão "Salvar e Novo" foi clicado
        if 'save_and_new' in self.request.POST:
            # Redirecionar para a tela de criação com os dados preenchidos
            # fields = ['foto', 'codigo', 'nome', 'observacao', 'tipo', 'quantidademin', 'quantidade', 'unidade']

            initial = {
                'codigo': form.cleaned_data['codigo'],
                'nome': form.cleaned_data['nome'],
                'observacao': form.cleaned_data['observacao'],
                'tipo': form.cleaned_data['tipo'],
                'quantidademin': form.cleaned_data['quantidademin'],
                'quantidade': form.cleaned_data['quantidade'],
                'unidade': form.cleaned_data['unidade'],
                'foto': form.cleaned_data['foto'],
            }
            form = ProdutoModelForm(initial=initial)
            context = {'form': form}
            return render(self.request, 'produto_form.html', context)


        return None
    # def get_initial(self):
    #     #if button is clicked
    #     if self.request.POST.get('salvar'):
    #         initial = super(ProdutoAddView, self).get_initial()
    #         initial['codigo'] = self.request.POST.get('codigo')
    #         initial['nome'] = self.request.POST.get('nome')
    #         initial['descricao'] = self.request.POST.get('descricao')
    #         initial['preco'] = self.request.POST.get('preco')
    #         initial['quantidade'] = self.request.POST.get('quantidade')
    #         return initial


class ProdutoEditRemov(ListView):
    model = Produto
    template_name = 'editremov.html'

    def get_queryset(self, *args, **kwargs):
        buscar = self.request.GET.get('buscar')
        qs = super(ProdutoEditRemov, self).get_queryset(*args, **kwargs)  # Correção aqui
        if buscar:
            qs = qs.filter(nome__icontains=buscar)

        paginator = Paginator(qs, 2)
        listagem = paginator.get_page(self.request.GET.get('page'))
        return listagem
class ProdutoUpDateView(UpdateView):
    form_class = ProdutoModelForm
    model = Produto
    template_name = 'produto_form.html'
    success_url = reverse_lazy('produtos')
class ProdutoDeleteView(DeleteView):
    model = Produto
    template_name = 'produto_apagar.html'
    success_url = reverse_lazy('produtos')