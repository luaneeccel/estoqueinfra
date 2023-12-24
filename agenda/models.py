from django.db import models

# Create your models here.
class Auditorio(models.Model):
    # atributos da classe auditorio
    nome = models.CharField('Nome', max_length=50, help_text='Nome do auditório.')

    class Meta:
        verbose_name = 'Auditório'
        verbose_name_plural = 'Auditórios'

    def __str__(self):
        return self.nome

class Agenda(models.Model):
    # atributos da classe agenda
    AUDITORIOS_OPCOES = (
        ('ARQ', 'Arquitetura'),
        ('IN', 'INPE'),
        ('AN', 'Pércio Reis'),
        ('WA', 'Wilson Aita'),
        ('S127', 'Sala 127'),
        ('S132', 'Sala 132'),
        #('S234', 'Sala 234'),
        #('S321', 'Sala 321'),
        ('S355', 'Sala 355'),
        #('S1305', 'Sala 1305')
    )
    status_choices = (
        ('contato', 'Entrar em contato'),
        ('arrumar', 'Arrumar auditório'),
        ('pronto', 'Tudo pronto'),
    )


    auditorio = models.ForeignKey(Auditorio, on_delete=models.CASCADE, verbose_name='Auditório', help_text='Auditório', default='')

    # auditorio = models.CharField('Auditório', max_length=50, help_text='Auditório', choices=AUDITORIOS_OPCOES,
    #                              default='')
    observacao = models.CharField('Observação', max_length=100, help_text='Observação sobre o agendamento.', blank=True)

    status = models.CharField('Status', max_length=50, help_text='Status do agendamento', choices=status_choices,
                             default='contato')

    evento = models.CharField('Nome Evento',max_length=255, help_text='Nome do evento.',default='', blank=True)
    numero_pessoas = models.IntegerField('Número de pessoas', help_text='Número de pessoas.',default=0, blank=True)
    solicitante = models.CharField('Nome Solicitante',max_length=255, help_text='Nome do solicitante.',default='', blank=True)
    contato = models.CharField('Contato Solicitante',max_length=155, help_text='Contato do solicitante.',default='', blank=True)
    equipamento = models.TextField('Equipamentos', help_text='Lista de equipamentos necessários.',default='', blank=True)
    data = models.DateField('Data', help_text='Data do evento.',default='', blank=True)
    hora_inicio = models.TimeField('Hora Início', help_text='Hora de início do evento.',default='', blank=True)
    hora_fim = models.TimeField('Hora Fim', help_text='Hora de fim do evento.',default='', blank=True)


    class Meta:
        verbose_name = 'Agendamento'
        verbose_name_plural = 'Agendamentos'

    def __str__(self):
        return f'Auditório: {self.auditorio} - Evento: {self.evento}'