from django.contrib import admin
from .models import Restaurante, Funcionario, Produto, Cupom

@admin.register(Restaurante)
class RestauranteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cnpj', 'ativo', 'modo_pausa', 'data_criacao')
    search_fields = ('nome', 'cnpj')


@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('user', 'restaurante', 'cargo')
    search_fields = ('user__username', 'restaurante__nome')


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'restaurante', 'preco', 'estoque', 'disponivel')
    list_filter = ('disponivel', 'restaurante')
    search_fields = ('nome',)


@admin.register(Cupom)
class CupomAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'restaurante', 'desconto_percentual', 'validade', 'ativo')
    list_filter = ('ativo', 'validade')
    search_fields = ('codigo',)
