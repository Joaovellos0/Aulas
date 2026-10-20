from django.contrib import admin
from .models import Marca, TipoGuitarra, Guitarra


@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ("marca", "slug")
    prepopulated_fields = {"slug": ("marca",)}
    search_fields = ("marca",)


@admin.register(TipoGuitarra)
class TipoGuitarraAdmin(admin.ModelAdmin):
    list_display = ("nome", "slug")
    prepopulated_fields = {"slug": ("nome",)}
    search_fields = ("nome",)


@admin.register(Guitarra)
class GuitarraAdmin(admin.ModelAdmin):
    list_display = ("modelo", "marca", "tipo", "preco", "disponibilidade", "em_destaque")
    list_filter = ("marca", "tipo", "disponibilidade", "em_destaque")
    search_fields = ("modelo", "marca__marca", "descricao")
    prepopulated_fields = {"slug": ("modelo",)}
