from django.urls import path
from .views import AgendasView, AgendaAddView, AgendaUpDateView, AgendaDeleteView

urlpatterns = [
    path('agendas', AgendasView.as_view(), name='agendas'),
    path('agenda/adicionar/', AgendaAddView.as_view(), name='agenda_adicionar'),
    path('<int:pk>/agenda/editar/', AgendaUpDateView.as_view(), name='agenda_editar'),
    path('<int:pk>/agenda/apagar/', AgendaDeleteView.as_view(), name='agenda_apagar'),
]
