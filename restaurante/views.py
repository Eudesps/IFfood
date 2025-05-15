from django.shortcuts import render
from .models import Restaurante


# Create your views here.
def index(request):
    restaurantes = Restaurante.objects.all()
    
    return render(request, 'index.html', {'restaurantes': restaurantes})

