from django.shortcuts import render

# Create your views here.
#def index(request):
#    return render(request, 'index.html')
from django.views.generic import TemplateView
class IndexView(TemplateView):
    template_name='index.html'