from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from .models import Agenda
from .forms import AgendaListForm, AgendaModelForm

from datetime import date, timedelta

from django.contrib import admin
from django.utils.translation import gettext_lazy as _


# from home.utils import HtmlToPdf
# from .models import Cliente


class AgendasView(ListView):
    model = Agenda
    template_name = 'agendas.html'

    def get_context_data(self, **kwargs):
        context = super(AgendasView, self).get_context_data(**kwargs)

        if self.request.GET:
            form = AgendaListForm(self.request.GET)
        else:
            form = AgendaListForm()

        context['form'] = form

        return context

    def get_queryset(self, *args, **kwargs):
        buscar = self.request.GET.get('buscar')
        qs = super(AgendasView, self).get_queryset(*args, **kwargs)
        qs2 = qs

        if self.request.GET:
            form = AgendaListForm(self.request.GET)
            if form.is_valid():
                auditorio = form.cleaned_data.get('auditorio')
                status = form.cleaned_data.get('status')
                filtro_tempo = form.cleaned_data.get('filtro_tempo')

                if filtro_tempo == 'dia':
                    qs = qs.filter(data=date.today())
                elif filtro_tempo == 'mes':
                    qs = qs.filter(data__month=date.today().month, data__year=date.today().year)
                elif filtro_tempo == 'semana':
                    today = date.today()
                    sunday = today - timedelta(days=today.isoweekday())
                    saturday = sunday + timedelta(days=6)
                    qs = qs.filter(data__range=[sunday, saturday])
                elif filtro_tempo == 'td':
                   qs = qs2

                if auditorio:
                    qs = qs.filter(auditorio=auditorio)

                if status:
                    qs = qs.filter(status__icontains=status)
                if buscar:
                    qs = qs.filter(Q(solicitante__icontains=buscar)) | qs.filter(Q(evento__icontains=buscar))

        if qs.count() > 0:
            paginator = Paginator(qs, 10)
            listagem = paginator.get_page(self.request.GET.get('page'))
            return listagem
        else:
            messages.info(self.request, "Não existem agendamentos cadastrados!")
            return qs

    # def get(self, *args, **kwargs):
    #     if self.request.GET.get('imprimir') == 'pdf':
    #         html_pdf = HtmlToPdf(arquivo='agendas_pdf', qs=self.get_queryset())
    #         return html_pdf.response
    #     else:
    #         return super(AgendasView, self).get(*args, **kwargs)


#
class AgendaAddView(SuccessMessageMixin, CreateView):
    form_class = AgendaModelForm
    model = Agenda
    template_name = 'agenda_form.html'
    success_url = reverse_lazy('agendas')
    success_message = 'Agendamento cadastrado com sucesso!'

    #     # se o botao "salvar e continuar" for clicado, ele vai pegar os dados da ultima criação e redirecionar para a pagina de criação de agendamento com os dados preenchidos
    #
    #     # inserir os dados e redirecione para a pagina de criação de agendamento com os dados preenchidos da ultima criação
    def form_valid(self, form):
        # Lógica padrão de validação do formulário
        response = super().form_valid(form)
        # Se o botão "Salvar e Novo" foi clicado
        if 'save_and_new' in self.request.POST:
            # Redirecionar para a tela de criação com os dados preenchidos

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
            form = AgendaModelForm(initial=initial)
            context = {'form': form}
            from django.shortcuts import render
            return render(self.request, 'agenda_form.html', context)


#     def get_initial(self):
#         #if button is clicked
#         if self.request.POST.post('salvar'):
#             initial = super(AgendaAddView, self).get_initial()
#             initial['auditorio'] = self.request.GET.get('auditorio')
#             initial['requester_name'] = self.request.GET.get('requester_name')
#             initial['event_name'] = self.request.GET.get('event_name')
#             initial['requester_contact'] = self.request.GET.get('requester_contact')
#             initial['number_of_people'] = self.request.GET.get('number_of_people')
#             initial['observacao'] = self.request.GET.get('observacao')
#             return initial
#

class AgendaUpDateView(SuccessMessageMixin, UpdateView):
    form_class = AgendaModelForm
    model = Agenda
    template_name = 'agenda_form.html'
    success_url = reverse_lazy('agendas')
    success_message = 'Agendamento alterado com sucesso!'


class AgendaDeleteView(SuccessMessageMixin, DeleteView):
    model = Agenda
    template_name = 'agenda_apagar.html'
    success_url = reverse_lazy('agendas')
    success_message = 'Agendamento excluído com sucesso!'
