# Generated by Django 4.1.5 on 2023-12-19 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0002_alter_agenda_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda',
            name='auditorio',
            field=models.CharField(choices=[('ARQ', 'Arquitetura'), ('IN', 'INPE'), ('AN', 'Pércio Reis'), ('WA', 'Wilson Aita'), ('S127', 'Sala 127'), ('S132', 'Sala 132'), ('S355', 'Sala 355')], default='', help_text='Auditório', max_length=50, verbose_name='Auditório'),
        ),
    ]
