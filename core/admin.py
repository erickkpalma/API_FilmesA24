from django.contrib import admin
from .models import FilmesA24Model, ComentariosModel

@admin.register(FilmesA24Model)
class FilmesRegister(admin.ModelAdmin):
    list_display = [
        'titulo', 'diretor', 'lancamento'
    ]

@admin.register(ComentariosModel)
class ComentariosRegister(admin.ModelAdmin):
    list_display = [
        'filme', 'nome', 'comentario'
    ]
