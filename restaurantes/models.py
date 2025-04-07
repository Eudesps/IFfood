from django.db import models
from django.contrib.auth.models import User

class Restaurante(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    cnpj = models.CharField(max_length=18, unique=True)
    ativo = models.BooleanField(default=True)
    modo_pausa = models.BooleanField(default=False)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome


class Funcionario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE, related_name='funcionarios')
    cargo = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.user.username} - {self.cargo}"


class Produto(models.Model):
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE, related_name='produtos')
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    estoque = models.IntegerField(default=0)
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return self.nome


class Cupom(models.Model):
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE, related_name='cupons')
    codigo = models.CharField(max_length=20, unique=True)
    desconto_percentual = models.DecimalField(max_digits=5, decimal_places=2)
    validade = models.DateTimeField()
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.codigo
