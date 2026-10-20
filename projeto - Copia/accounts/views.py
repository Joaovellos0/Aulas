from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Usuario


# Create your views here.
def cadastrar(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        email = request.POST.get("email")
        senha = request.POST.get("senha")
        telefone = request.POST.get("telefone")
        pais = request.POST.get("pais")
        estado = request.POST.get("estado")
        cidade = request.POST.get("cidade")
        bairro = request.POST.get("bairro")
        numero = request.POST.get("numero")
        complemento = request.POST.get("complemento")

        usuario = User.objects.create_user(username=nome, email=email, password=senha)
        Usuario.objects.create(
            usuario=usuario,
            telefone=telefone,
            pais=pais,
            estado=estado,
            cidade=cidade,
            bairro=bairro,
            numero=numero,
            complemento=complemento,
        )
        return redirect("login")

    else:
        return render(request, "cadastro.html")


def logar(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        senha = request.POST.get("senha")

        usuario = authenticate(request, username=nome, password=senha)
        if usuario is not None:
            login(request, usuario)
            return redirect("home")
        else:
            messages.error(request, "Usuário ou senha incorretos.")
            return render(request, "login.html")
    else:
        return render(request, "login.html")
