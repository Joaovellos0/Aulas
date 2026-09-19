from django.urls import path
from core import views

urlpatterns = [
    path('', views.home, name="home"),
    path('sobre', views.sobre, name="sobre"),
    path('contatos', views.contatos, name="contatos")
]
