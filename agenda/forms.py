from django import forms

from .models import Agenda, Auditorio

from datetime import date, timedelta

from django.contrib import admin
from django.utils.translation import gettext_lazy as _


#
#
# class DataListFilter(admin.SimpleListFilter):
#     title = _("Espaço de tempo")
#     parameter_name = 'data'
#
#     def lookups(self, request, model_admin):
#         return (
#             ('mes', _('Eventos do Mês')),
#             ('semana', _('Eventos da Semana')),
#         )
#
#     def queryset(self, request, queryset):
#
#         if self.value() == 'semana':
#             today = date.today()
#             sunday = today - timedelta(days=today.isoweekday())
#             saturday = sunday + timedelta(days=6)
#             return queryset.filter(data__range=[sunday, saturday])
#
#         if self.value() == 'mes':
#             return queryset.filter(data__month=date.today().month, data__year=date.today().year)


class AgendaListForm(forms.Form):

    status_choices = (
        ('contato', 'Entrar em contato'),
        ('arrumar', 'Arrumar auditório'),
        ('pronto', 'Tudo pronto'),
    )

    filtro_tempo_choices = (
        ('td', 'Todos os Eventos'),
        ('dia', 'Eventos do Dia'),
        ('semana', 'Eventos da Semana'),
        ('mes', 'Eventos do Mês'),

    )

    TERMO_CHOICES = (
        ('N', 'Não'),
        ('S', 'Sim')
    )

    data = forms.DateField(label='Data: ', widget=forms.DateInput(
        attrs={'class': 'input', 'placeholder': 'Digite a data do evento'}), required=False)
    auditorio = forms.ModelChoiceField(label='Auditório:', widget=forms.Select(
        attrs={'class': 'select is-fullwidth'}), queryset=Auditorio.objects.all(), required=False)

    status = forms.ChoiceField(label='Status:', widget=forms.Select(
        attrs={'class': 'select is-fullwidth'}), choices=status_choices, required=False)

    filtro_tempo = forms.ChoiceField(label='Filtro de Tempo:', widget=forms.Select(
        attrs={'class': 'select is-fullwidth'}), choices=filtro_tempo_choices, required=False)

    evento = forms.CharField(label='Nome do Evento:', widget=forms.TextInput(
        attrs={'class': 'input', 'placeholder': 'Digite o nome do evento'}), required=False)

    solicitante = forms.CharField(label='Nome do Solicitante:', widget=forms.TextInput(
        attrs={'class': 'input', 'placeholder': 'Digite o nome do solicitante'}), required=False)

    contato = forms.CharField(label='Contato do Solicitante:', widget=forms.TextInput(
        attrs={'class': 'input', 'placeholder': 'Digite o contato do solicitante'}), required=False)

    equipamento = forms.CharField(label='Equipamentos:', widget=forms.TextInput(
        attrs={'class': 'input', 'placeholder': 'Digite os equipamentos'}), required=False)

    hora_inicio = forms.TimeField(label='Hora de Início:', widget=forms.TimeInput(
        attrs={'class': 'input', 'placeholder': 'Digite a hora de início'}), required=False)

    hora_fim = forms.TimeField(label='Hora de Fim:', widget=forms.TimeInput(
        attrs={'class': 'input', 'placeholder': 'Digite a hora de fim'}), required=False)

    numero_pessoas = forms.IntegerField(label='Quantidade de Pessoas:', widget=forms.NumberInput(
        attrs={'class': 'input', 'placeholder': 'Digite a quantidade de pessoas'}), required=False)

    termo = forms.ChoiceField(label='Termo de Responsabilidade:', widget=forms.Select(
        attrs={'class': 'select is-fullwidth'}), choices=TERMO_CHOICES, required=False)
#
class AgendaModelForm(forms.ModelForm):
    class Meta:
        model = Agenda
        fields = ['auditorio', 'evento', 'solicitante', 'data', 'hora_inicio', 'hora_fim',
                  'numero_pessoas', 'contato', 'termo', 'status',
                  'equipamento']
        #
        widgets = {
            'auditorio': forms.Select(attrs={'class': 'input', 'placeholder': 'Selecione o auditório'}),
            'status': forms.Select(attrs={'class': 'input', 'placeholder': 'Selecione o status'}),
            'evento': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Digite o nome do evento'}),
            'numero_pessoas': forms.NumberInput(
                attrs={'class': 'input', 'placeholder': 'Digite a quantidade de pessoas'}),
            'solicitante': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Digite o nome do solicitante'}),
            'contato': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Digite o contato do solicitante'}),
            'equipamento': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Digite os equipamentos'}),
            'data': forms.DateInput(
                attrs={'class': 'input', 'type': 'date', 'placeholder': 'Digite a data do agendamento'}),
            'hora_inicio': forms.TimeInput(
                attrs={'class': 'input', 'type': 'time', 'placeholder': 'Digite a hora de início'}),
            'hora_fim': forms.TimeInput(
                attrs={'class': 'input', 'type': 'time', 'placeholder': 'Digite a hora de fim'}),
            'termo': forms.Select(
                attrs={'class': 'input', 'placeholder': 'Selecione o status do termo de responsabilidade'}),

        }
