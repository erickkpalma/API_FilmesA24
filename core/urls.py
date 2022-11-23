from django.urls import path
from .views import (FilmesAPIView,
                    FilmeAPIView,
                    ComentariosAPIView,
                    ComentarioAPIView,
                    FilmesView, ComentariosView)
from rest_framework.routers import SimpleRouter

""" Rotas com SimpleRouter """

router = SimpleRouter()
router.register('filmes', FilmesView)
router.register('comentarios', ComentariosView)

""" Rotas sem SimpleRouter """

urlpatterns = [
    path('filmes/', FilmesAPIView.as_view(), name='filmes'),
    path('filmes/<int:pk>/', FilmeAPIView.as_view(), name='filme'),
    path('filmes/<int:filme_pk>/comentarios/', ComentariosAPIView.as_view(), name='filme_comentarios'),
    path('filmes/<int:filme_pk>/comentarios/<int:comentario_pk>', ComentarioAPIView.as_view(), name='filme_comentarios'),

    path('comentarios/', ComentariosAPIView.as_view(), name='comentarios'),
    path('comentarios/<int:comentario_pk>/', ComentarioAPIView.as_view(), name='comentario')

]