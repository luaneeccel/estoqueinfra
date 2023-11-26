from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse_lazy

# Create your views here.
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import Produto
from .forms import ProdutoModelForm
class ProdutoView(ListView):
    model = Produto
    template_name = 'produto.html'

    def get_queryset(self, *args, **kwargs):
        buscar = self.request.GET.get('buscar')
        qs = super(ProdutoView, self).get_queryset(*args, **kwargs)
        if buscar:
            qs = qs.filter(nome__icontains=buscar)

        paginator= Paginator (qs, 2)
        listagem =paginator.get_page(self.request.GET.get('page'))
        return listagem
class ProdutoAddView(CreateView):
    form_class = ProdutoModelForm
    model = Produto
    template_name = 'produto_form.html'
    success_url = reverse_lazy('produtos')



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