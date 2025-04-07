from rest_framework import serializers
from .models import Restaurante, Funcionario, Produto, Cupom
from django.contrib.auth.models import User

class RestauranteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurante
        fields = '__all__'


class FuncionarioSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Funcionario
        fields = '__all__'


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'


class CupomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cupom
        fields = '__all__'
