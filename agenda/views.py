from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from .models import Agenda
from .forms import AgendaListForm, AgendaModelForm
from django.shortcuts import redirect
from datetime import date, timedelta
from django.shortcuts import render
from django.shortcuts import get_object_or_404
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
class AgendaAddView(CreateView):
    form_class = AgendaModelForm
    model = Agenda
    template_name = 'agenda_form.html'
    success_url = reverse_lazy('agendas')

    def form_valid(self, form):
        # If the 'save_and_new' button is clicked
        if 'save_and_new' in self.request.POST:
            # Save the form data and then render a new form with the initial data
            self.object = form.save(commit=False)

            # Make sure to include the 'data' field in the initial data
            initial_data = {
                'auditorio': form.cleaned_data['auditorio'],
                'evento': form.cleaned_data['evento'],
                'solicitante': form.cleaned_data['solicitante'],
                'numero_pessoas': form.cleaned_data['numero_pessoas'],
                'contato': form.cleaned_data['contato'],
                'status': form.cleaned_data['status'],
                'data': form.cleaned_data['data'],
                'equipamento': form.cleaned_data['equipamento'],
            }

            # Set the 'data' field on the instance before saving
            self.object.data = initial_data['data']

            # Save the instance
            self.object.save()

            # Create a new form with the initial data
            form = AgendaModelForm(initial=initial_data)
            context = {'form': form}
            return render(self.request, 'agenda_form.html', context)
        else:
            # If the 'save' button is clicked, proceed with the default behavior
            return super().form_valid(form)


class AgendaUpDateView(SuccessMessageMixin, UpdateView):
    form_class = AgendaModelForm
    model = Agenda
    template_name = 'agenda_form.html'
    success_url = reverse_lazy('agendas')
    success_message = 'Agendamento alterado com sucesso!'

    def form_valid(self, form):
        # If the 'save_and_new' button is clicked
        if 'save_and_new' in self.request.POST:
            # Create a new instance with the same data and save it
            new_agenda = form.save(commit=False)
            new_agenda.pk = None  # Set the primary key to None to create a new instance
            new_agenda.save()

            # Redirect to edit the new instance
            return redirect('agenda_editar', pk=new_agenda.pk)
        else:
            # If the 'save' button is clicked, proceed with the default behavior
            return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['duplicate'] = True  # Add a flag to indicate duplication
        return context

    def get(self, request, *args, **kwargs):
        # Override get method to handle the 'duplicate' parameter in the URL
        if 'duplicate' in self.request.GET:
            # Load the existing agenda item to duplicate
            existing_agenda = get_object_or_404(Agenda, pk=self.kwargs['pk'])
            # Populate the form with existing data
            form = self.get_form(instance=existing_agenda)
            # Render the form with the 'duplicate' flag
            return render(request, 'agenda_form.html', {'form': form, 'duplicate': True})
        else:
            return super().get(request, *args, **kwargs)
class AgendaDeleteView(SuccessMessageMixin, DeleteView):
    model = Agenda
    template_name = 'agenda_apagar.html'
    success_url = reverse_lazy('agendas')
    success_message = 'Agendamento excluído com sucesso!'
