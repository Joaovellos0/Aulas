from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

def sobre(request):
    return render(request, 'sobre.html')

def contatos(request):
    return render(request, 'contatos.html')