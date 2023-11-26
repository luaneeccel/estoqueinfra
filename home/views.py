from django.shortcuts import render

# Create your views here.
#def index(request):
#    return render(request, 'index.html')
from django.views.generic import TemplateView
from django.db.models import F

from produto.models import Produto
class IndexView(TemplateView):
    template_name='index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['qtd_produtos'] = Produto.objects.count()
        context['min_produtos'] =  Produto.objects.filter(quantidade__lt=F('quantidademin'),quantidade__gt=0).count()
        context['zero_produtos'] = Produto.objects.filter(quantidade=0).count()
        return context