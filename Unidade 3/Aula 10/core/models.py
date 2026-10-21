from django.db import models

# Create your models here.

class Produto(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    disponivel = models.BooleanField(default=True)
