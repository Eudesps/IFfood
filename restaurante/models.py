from django.db import models

# Create your models here.
class Restaurante(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.nome