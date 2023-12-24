from django.contrib import admin

# Register your models here.


from .models import Agenda, Auditorio
from django.utils.html import format_html
from datetime import date, timedelta

from django.contrib import admin
from django.utils.translation import gettext_lazy as _


class DataListFilter(admin.SimpleListFilter):
    title = _("Espaço de tempo")
    parameter_name = 'data'

    def lookups(self, request, model_admin):
        return (
            ('mes', _('Eventos do Mês')),
            ('semana', _('Eventos da Semana')),
        )

    def queryset(self, request, queryset):

        if self.value() == 'semana':
            today = date.today()
            sunday = today - timedelta(days=today.isoweekday())
            saturday = sunday + timedelta(days=6)
            return queryset.filter(data__range=[sunday, saturday])

        if self.value() == 'mes':
            return queryset.filter(data__month=date.today().month, data__year=date.today().year)


@admin.register(Auditorio)
class AuditorioAdmin(admin.ModelAdmin):
    fields = ('nome',)
    list_display = ['nome']
    search_fields = ('nome',)
    search_help_text = ('Pesquisa por Nome')
    ordering = ('nome',)
    list_filter = ('nome',)


@admin.register(Agenda)
class AgendaAdmin(admin.ModelAdmin):
    fields = (
        'data', 'hora_inicio', 'hora_fim', 'auditorio', 'evento', 'solicitante', 'contato', 'equipamento', 'status',
        'numero_pessoas', 'observacao')

    list_display = [
        'data', 'horario', 'auditorio', 'evento', 'solicitante', 'contato', 'equipamento', 'status',
        'numero_pessoas', 'observacao']
    search_fields = ('solicitante', 'evento')
    search_help_text = ('Pesquisa por Solicitante ou Evento')
    ordering = ('data', 'hora_inicio',)

    list_filter = ('auditorio', 'status', DataListFilter)

    def horario(self, obj):
        return f'{obj.hora_inicio} às {obj.hora_fim}'
