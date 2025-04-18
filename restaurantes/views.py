from rest_framework import viewsets
from .models import Restaurante, Funcionario, Produto, Cupom
from .serializers import RestauranteSerializer, FuncionarioSerializer, ProdutoSerializer, CupomSerializer
from django.shortcuts import render

class RestauranteViewSet(viewsets.ModelViewSet):
    queryset = Restaurante.objects.all()
    serializer_class = RestauranteSerializer

class FuncionarioViewSet(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    

class CupomViewSet(viewsets.ModelViewSet):
    queryset = Cupom.objects.all()
    serializer_class = CupomSerializer
    
def homepage(request):
    return render(request, 'restaurantes/index.html')
