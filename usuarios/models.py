from django.db import models

# Create your models here.
class Usuario(models.Model):
    
    nome = models.CharField(max_length=100)
    senha = models.CharField(max_length=512)
    email = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    telefone = models.CharField(max_length=16)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    
    def __str__(self):
         return self.nome
    
