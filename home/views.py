from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
# def index(request):
#    return render(request, 'index.html')
from django.views.generic import TemplateView
from django.db.models import F
from django.contrib import admin
from produto.models import Produto

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate

def login(request):
    if request.method == 'POST':
        usuario = request.POST['usuario']
        senha = request.POST['senha']
        user = authenticate(request, username=usuario, password=senha)

        if user is not None:
            # Autenticação bem-sucedida
            return redirect('index')
        else:
            # Autenticação falhou
            return render(request, 'login.html', {'erro': 'Credenciais inválidas'})
    return render(request, 'login.html')

def pagina_destino(request):
    return render(request, 'index.html')

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['qtd_produtos'] = Produto.objects.count()
        context['min_produtos'] = Produto.objects.filter(quantidade__lt=F('quantidademin'), quantidade__gt=0).count()
        context['zero_produtos'] = Produto.objects.filter(quantidade=0).count()
        return context
