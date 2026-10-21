from django.shortcuts import render
from .models import Solucao

# Create your views here.
def home(request):
    return render(request, 'home.html')

def solucoes(request):
    lista_de_solucoes = Solucao.objects.all()
    return render(request, 'solucoes.html', {'lista_solucoes': lista_de_solucoes})

def sobre(request):
    return render(request, 'sobre.html')

def login(request):
    return render(request, 'login.html')


