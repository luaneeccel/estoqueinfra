from django.db import models

# Create your models here.
class Usuario(models.Model):
    nome_usuario=models.CharField(max_length=50)
    senha = models.CharField(max_length=50)